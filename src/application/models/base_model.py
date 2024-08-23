from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class BaseModel(ABC):
    """
    Abstract base class for all language models.

    This class defines the interface that all specific model implementations should follow.
    It includes methods for text generation, embedding creation, and model information retrieval.

    Attributes:
        model_name (str): The name of the model.

    Methods:
        generate: Generate text based on a given prompt.
        create_embedding: Create an embedding for a given text.
        get_model_info: Retrieve information about the model.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    async def generate(self, prompt: str, max_tokens: int = 100, temperature: float = 0.7, 
                       top_p: float = 1.0, n: int = 1, stop: Optional[List[str]] = None, 
                       presence_penalty: float = 0.0, frequency_penalty: float = 0.0, 
                       logit_bias: Optional[Dict[str, float]] = None) -> str:
        """
        Generate text based on the given prompt.

        Args:
            prompt (str): The input prompt for text generation.
            max_tokens (int): The maximum number of tokens to generate.
            temperature (float): Controls randomness in generation. Higher values mean more random completions.
            top_p (float): Controls diversity via nucleus sampling.
            n (int): How many completions to generate for each prompt.
            stop (Optional[List[str]]): Up to 4 sequences where the API will stop generating further tokens.
            presence_penalty (float): Positive values penalize new tokens based on whether they appear in the text so far.
            frequency_penalty (float): Positive values penalize new tokens based on their existing frequency in the text so far.
            logit_bias (Optional[Dict[str, float]]): Modify the likelihood of specified tokens appearing in the completion.

        Returns:
            str: The generated text.
        """
        pass

    @abstractmethod
    async def create_embedding(self, text: str) -> List[float]:
        """
        Create an embedding for the given text.

        Args:
            text (str): The input text to create an embedding for.

        Returns:
            List[float]: The embedding vector.
        """
        pass

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """
        Retrieve information about the model.

        Returns:
            Dict[str, Any]: A dictionary containing model information such as name, version, capabilities, etc.
        """
        pass