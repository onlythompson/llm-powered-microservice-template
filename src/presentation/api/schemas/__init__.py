"""
API Schemas Module

This module contains Pydantic models that define the structure of request and response
bodies for the LLM-powered microservice API. These schemas are used for validation,
serialization, and OpenAPI (Swagger) documentation.

Components:
- LLMRequestSchema: Schema for LLM generation requests
- LLMResponseSchema: Schema for LLM generation responses
- TextSummarizationRequestSchema: Schema for text summarization requests

Usage:
    from presentation.api.schemas import LLMRequestSchema, LLMResponseSchema

    @app.post("/generate", response_model=LLMResponseSchema)
    async def generate_text(request: LLMRequestSchema):
        # Use the validated request data
        ...
"""

from .llm_request import LLMRequestSchema, TextSummarizationRequestSchema
from .llm_response import LLMResponseSchema

__all__ = ["LLMRequestSchema", "LLMResponseSchema", "TextSummarizationRequestSchema"]

# Version of the schemas module
__version__ = "0.1.0"