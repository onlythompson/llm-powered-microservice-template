from pydantic import BaseModel, Field
from typing import List, Optional

class LLMChoiceSchema(BaseModel):
    """
    Schema for a single LLM generation choice.

    This schema represents a single completion choice returned by the language model.

    Attributes:
        text (str): The generated text.
        index (int): The index of this completion choice.
        logprobs (Optional[float]): Log probabilities of the tokens in the completion.
        finish_reason (Optional[str]): The reason why the completion finished.
    """

    text: str = Field(..., description="The generated text")
    index: int = Field(..., description="The index of this completion choice")
    logprobs: Optional[float] = Field(None, description="Log probabilities of the tokens in the completion")
    finish_reason: Optional[str] = Field(None, description="The reason why the completion finished")

class LLMUsageSchema(BaseModel):
    """
    Schema for token usage information.

    This schema represents the token usage for a completion request.

    Attributes:
        prompt_tokens (int): The number of tokens in the prompt.
        completion_tokens (int): The number of tokens in the completion.
        total_tokens (int): The total number of tokens used.
    """

    prompt_tokens: int = Field(..., ge=0, description="The number of tokens in the prompt")
    completion_tokens: int = Field(..., ge=0, description="The number of tokens in the completion")
    total_tokens: int = Field(..., ge=0, description="The total number of tokens used")

class LLMResponseSchema(BaseModel):
    """
    Schema for LLM generation responses.

    This schema defines the structure of the response body for LLM text generation endpoints.

    Attributes:
        id (str): A unique identifier for the response.
        object (str): The object type, which is typically "text_completion".
        created (int): The Unix timestamp of when the response was created.
        model (str): The name of the model used to generate the response.
        choices (List[LLMChoiceSchema]): A list of completion choices.
        usage (LLMUsageSchema): Token usage information for the request and response.
    """

    id: str = Field(..., description="A unique identifier for the response")
    object: str = Field("text_completion", description="The object type")
    created: int = Field(..., description="The Unix timestamp of when the response was created")
    model: str = Field(..., description="The name of the model used to generate the response")
    choices: List[LLMChoiceSchema] = Field(..., description="A list of completion choices")
    usage: LLMUsageSchema = Field(..., description="Token usage information for the request and response")

    class Config:
        schema_extra = {
            "example": {
                "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
                "object": "text_completion",
                "created": 1589478378,
                "model": "gpt-3.5-turbo",
                "choices": [
                    {
                        "text": "Once upon a time, there was a brave princess who...",
                        "index": 0,
                        "logprobs": None,
                        "finish_reason": "length"
                    }
                ],
                "usage": {
                    "prompt_tokens": 5,
                    "completion_tokens": 100,
                    "total_tokens": 105
                }
            }
        }