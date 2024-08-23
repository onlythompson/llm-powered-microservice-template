from pydantic import BaseModel, Field
from typing import Optional, List

class LLMRequestSchema(BaseModel):
    """
    Schema for LLM generation requests.

    This schema defines the structure of the request body for LLM text generation endpoints.
    It includes various parameters that control the behavior of the language model.

    Attributes:
        prompt (str): The input prompt for text generation.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): Controls randomness in generation. Higher values mean more random completions.
        top_p (float): Controls diversity via nucleus sampling.
        n (int): How many completions to generate for each prompt.
        stop (Optional[List[str]]): Up to 4 sequences where the API will stop generating further tokens.
        presence_penalty (float): Positive values penalize new tokens based on whether they appear in the text so far.
        frequency_penalty (float): Positive values penalize new tokens based on their existing frequency in the text so far.
    """

    prompt: str = Field(..., description="The input prompt for text generation")
    max_tokens: int = Field(100, ge=1, le=2048, description="The maximum number of tokens to generate")
    temperature: float = Field(0.7, ge=0, le=1, description="Controls randomness in generation")
    top_p: float = Field(1.0, ge=0, le=1, description="Controls diversity via nucleus sampling")
    n: int = Field(1, ge=1, le=10, description="How many completions to generate for each prompt")
    stop: Optional[List[str]] = Field(None, max_items=4, description="Up to 4 sequences where the API will stop generating further tokens")
    presence_penalty: float = Field(0.0, ge=-2.0, le=2.0, description="Penalize new tokens based on whether they appear in the text so far")
    frequency_penalty: float = Field(0.0, ge=-2.0, le=2.0, description="Penalize new tokens based on their existing frequency in the text so far")

    class Config:
        schema_extra = {
            "example": {
                "prompt": "Once upon a time",
                "max_tokens": 100,
                "temperature": 0.7,
                "top_p": 1.0,
                "n": 1,
                "stop": ["\n"],
                "presence_penalty": 0.0,
                "frequency_penalty": 0.0
            }
        }

class TextSummarizationRequestSchema(BaseModel):
    """
    Schema for text summarization requests.

    This schema defines the structure of the request body for text summarization endpoints.

    Attributes:
        text (str): The input text to be summarized.
        max_length (int): The maximum length of the summary in words.
    """

    text: str = Field(..., min_length=10, description="The input text to be summarized")
    max_length: int = Field(100, ge=10, le=500, description="The maximum length of the summary in words")

    class Config:
        schema_extra = {
            "example": {
                "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                "max_length": 50
            }
        }