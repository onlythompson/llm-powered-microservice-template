class LLMServiceException(Exception):
    """
    Base exception class for LLM service-related errors.

    This exception should be used as a base class for more specific
    LLM service exceptions.

    Attributes:
        message (str): The error message.
        status_code (int): The HTTP status code associated with this error.
    """

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ModelNotFoundException(LLMServiceException):
    """
    Exception raised when a requested LLM model is not found.

    Attributes:
        model_name (str): The name of the model that was not found.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name
        message = f"Model '{model_name}' not found"
        super().__init__(message, status_code=404)

class PromptValidationError(LLMServiceException):
    """
    Exception raised when there's an error in prompt validation.

    Attributes:
        details (str): Additional details about the validation error.
    """

    def __init__(self, details: str):
        message = f"Prompt validation error: {details}"
        super().__init__(message, status_code=400)

class LLMProviderError(LLMServiceException):
    """
    Exception raised when there's an error with the LLM provider service.

    Attributes:
        provider (str): The name of the LLM provider (e.g., "OpenAI", "Anthropic").
        details (str): Additional details about the error.
    """

    def __init__(self, provider: str, details: str):
        message = f"Error with LLM provider {provider}: {details}"
        super().__init__(message, status_code=502)  # Bad Gateway