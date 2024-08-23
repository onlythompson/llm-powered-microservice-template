from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class LLMRequest(BaseModel):
    """
    Represents a request to a Language Model (LLM).

    This class encapsulates all the parameters needed to make a request to an LLM,
    including the prompt, model selection, and various generation parameters.

    Attributes:
        prompt (str): The input prompt for the LLM.
        model (str): The name or identifier of the LLM to use.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): Controls randomness in generation. Higher values mean more random completions.
        top_p (float): Controls diversity via nucleus sampling.
        n (int): How many completions to generate for each prompt.
        stream (bool): Whether to stream back partial progress.
        stop (Optional[str]): Up to 4 sequences where the API will stop generating further tokens.
        presence_penalty (float): Positive values penalize new tokens based on whether they appear in the text so far.
        frequency_penalty (float): Positive values penalize new tokens based on their existing frequency in the text so far.
        user (Optional[str]): A unique identifier representing your end-user.
        extra_params (Dict[str, Any]): Any additional parameters specific to certain models or use cases.

    Example:
        >>> request = LLMRequest(
        ...     prompt="Translate 'Hello' to French",
        ...     model="gpt-3.5-turbo",
        ...     max_tokens=50,
        ...     temperature=0.7
        ... )
        >>> print(request.model)
        'gpt-3.5-turbo'
    """

    prompt: str
    model: str
    max_tokens: int = Field(default=100, ge=1)
    temperature: float = Field(default=0.7, ge=0, le=1)
    top_p: float = Field(default=1.0, ge=0, le=1)
    n: int = Field(default=1, ge=1)
    stream: bool = False
    stop: Optional[str] = None
    presence_penalty: float = Field(default=0.0, ge=-2.0, le=2.0)
    frequency_penalty: float = Field(default=0.0, ge=-2.0, le=2.0)
    user: Optional[str] = None
    extra_params: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        """Pydantic config"""
        allow_population_by_field_name = True