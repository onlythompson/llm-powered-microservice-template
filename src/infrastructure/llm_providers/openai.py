import openai
from typing import List, Dict, Any, Optional
from .base import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    """
    Implementation of the LLM provider for OpenAI's GPT models.

    This class provides methods to interact with OpenAI's GPT models,
    including text generation and embedding creation.

    Attributes:
        api_key (str): The API key for authenticating with OpenAI's services.
        model (str): The specific GPT model to use (e.g., "gpt-3.5-turbo", "gpt-4").

    Methods:
        generate_text: Generate text using OpenAI's GPT models.
        create_embedding: Create an embedding using OpenAI's embedding models.
        get_provider_info: Retrieve information about the OpenAI provider.
    """

    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

    async def generate_text(self, prompt: str, max_tokens: int = 100, temperature: float = 0.7, 
                            top_p: float = 1.0, n: int = 1, stop: Optional[List[str]] = None, 
                            presence_penalty: float = 0.0, frequency_penalty: float = 0.0, 
                            logit_bias: Optional[Dict[str, float]] = None) -> str:
        """
        Generate text using OpenAI's GPT models.

        Args:
            prompt (str): The input prompt for text generation.
            max_tokens (int): The maximum number of tokens to generate.
            temperature (float): Controls randomness in generation.
            top_p (float): Controls diversity via nucleus sampling.
            n (int): How many completions to generate for each prompt.
            stop (Optional[List[str]]): Up to 4 sequences where the API will stop generating further tokens.
            presence_penalty (float): Penalize new tokens based on whether they appear in the text so far.
            frequency_penalty (float): Penalize new tokens based on their existing frequency in the text so far.
            logit_bias (Optional[Dict[str, float]]): Modify the likelihood of specified tokens appearing in the completion.

        Returns:
            str: The generated text.
        """
        response = await openai.Completion.acreate(
            engine=self.model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias
        )
        return response.choices[0].text.strip()

    async def create_embedding(self, text: str) -> List[float]:
        """
        Create an embedding using OpenAI's embedding models.

        Args:
            text (str): The input text to create an embedding for.

        Returns:
            List[float]: The embedding vector.
        """
        response = await openai.Embedding.acreate(
            input=[text],
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']

    def get_provider_info(self) -> Dict[str, Any]:
        """
        Retrieve information about the OpenAI provider.

        Returns:
            Dict[str, Any]: A dictionary containing provider information.
        """
        return {
            "name": "OpenAI",
            "model": self.model,
            "type": "GPT",
            "version": openai.__version__
        }