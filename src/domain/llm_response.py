from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class LLMChoice(BaseModel):
    """
    Represents a single completion choice in an LLM response.

    Attributes:
        text (str): The generated text.
        index (int): The index of this completion choice.
        logprobs (Optional[Dict[str, Any]]): Log probabilities of the tokens in the completion.
        finish_reason (Optional[str]): The reason why the completion finished.
    """
    text: str
    index: int
    logprobs: Optional[Dict[str, Any]] = None
    finish_reason: Optional[str] = None

class LLMUsage(BaseModel):
    """
    Represents the token usage information for an LLM request/response.

    Attributes:
        prompt_tokens (int): The number of tokens in the prompt.
        completion_tokens (int): The number of tokens in the completion.
        total_tokens (int): The total number of tokens used.
    """
    prompt_tokens: int = Field(..., ge=0)
    completion_tokens: int = Field(..., ge=0)
    total_tokens: int = Field(..., ge=0)

class LLMResponse(BaseModel):
    """
    Represents a response from a Language Model (LLM).

    This class encapsulates all the information returned by an LLM in response to a request,
    including the generated text(s), model information, and usage statistics.

    Attributes:
        id (str): A unique identifier for the response.
        object (str): The object type, which is typically "text_completion".
        created (int): The Unix timestamp of when the response was created.
        model (str): The name of the model used to generate the response.
        choices (List[LLMChoice]): A list of completion choices.
        usage (LLMUsage): Token usage information for the request and response.

    Example:
        >>> response = LLMResponse(
        ...     id="cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
        ...     object="text_completion",
        ...     created=1589478378,
        ...     model="gpt-3.5-turbo",
        ...     choices=[
        ...         LLMChoice(text="Bonjour", index=0, finish_reason="length")
        ...     ],
        ...     usage=LLMUsage(prompt_tokens=5, completion_tokens=1, total_tokens=6)
        ... )
        >>> print(response.choices[0].text)
        'Bonjour'
    """
    id: str
    object: str
    created: int
    model: str
    choices: List[LLMChoice]
    usage: LLMUsage

    class Config:
        """Pydantic config"""
        allow_population_by_field_name = True