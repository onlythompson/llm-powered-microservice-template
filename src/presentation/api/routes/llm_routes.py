from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from pydantic import BaseModel

from application.services.llm_orchestrator import LLMOrchestrator
from domain.llm_request import LLMRequest
from domain.llm_response import LLMResponse
from core.dependencies import get_llm_orchestrator
from core.cross_cutting import log_error, process_request

router = APIRouter()

class GenerateTextRequest(BaseModel):
    """Request model for text generation"""
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7
    top_p: float = 1.0
    n: int = 1

class SummarizeTextRequest(BaseModel):
    """Request model for text summarization"""
    text: str
    max_length: int = 100

@router.post("/generate", response_model=LLMResponse)
async def generate_text(
    request: GenerateTextRequest,
    orchestrator: LLMOrchestrator = Depends(get_llm_orchestrator)
) -> LLMResponse:
    """Generate text based on the given prompt."""
    try:
        llm_request = LLMRequest(
            prompt=request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            n=request.n
        )
        response = await process_request(orchestrator.process_request("generate", llm_request))
        return response
    except Exception as e:
        log_error(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize", response_model=LLMResponse)
async def summarize_text(
    request: SummarizeTextRequest,
    orchestrator: LLMOrchestrator = Depends(get_llm_orchestrator)
) -> LLMResponse:
    """Summarize the given text."""
    try:
        llm_request = LLMRequest(
            prompt=f"Summarize the following text in no more than {request.max_length} words:\n\n{request.text}",
            max_tokens=request.max_length * 2,
            temperature=0.7,
            top_p=1.0,
            n=1
        )
        response = await process_request(orchestrator.process_request("summarize", llm_request))
        return response
    except Exception as e:
        log_error(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models", response_model=Dict[str, Any])
async def list_models(
    orchestrator: LLMOrchestrator = Depends(get_llm_orchestrator)
) -> Dict[str, Any]:
    """List available LLM models."""
    try:
        models = await orchestrator.list_models()
        return {"models": models}
    except Exception as e:
        log_error(e)
        raise HTTPException(status_code=500, detail=str(e))