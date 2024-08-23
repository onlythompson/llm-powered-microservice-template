from typing import Any, Dict
from application.models import ModelFactory
from application.prompt_management import PromptRepository
from application.domain.llm_request import LLMRequest
from application.domain.llm_response import LLMResponse

class LLMOrchestrator:
    """
    A service class for orchestrating interactions with Language Models (LLMs).

    This class manages the process of selecting appropriate models, retrieving
    and formatting prompts, and coordinating the generation of responses from LLMs.

    Attributes:
        model_factory (ModelFactory): A factory for creating LLM instances.
        prompt_repo (PromptRepository): A repository for managing prompt templates.

    Methods:
        process_request: Process an LLM request and generate a response.
        _get_model: Get an appropriate model for a given request.
        _format_prompt: Retrieve and format a prompt for a given request.
    """

    def __init__(self, model_factory: ModelFactory, prompt_repo: PromptRepository):
        self.model_factory = model_factory
        self.prompt_repo = prompt_repo

    async def process_request(self, request_type: str, input_text: str, **kwargs) -> LLMResponse:
        """
        Process an LLM request and generate a response.

        This method coordinates the entire process of handling an LLM request,
        including selecting the appropriate model, formatting the prompt,
        and generating the response.

        Args:
            request_type (str): The type of request (e.g., "translate", "summarize").
            input_text (str): The input text to be processed.
            **kwargs: Additional parameters specific to the request type.

        Returns:
            LLMResponse: The generated response from the LLM.

        Raises:
            ValueError: If the request type is not supported.

        Example:
            >>> orchestrator = LLMOrchestrator(model_factory, prompt_repo)
            >>> response = await orchestrator.process_request("translate", "Hello, world!", target_language="French")
            >>> print(response.choices[0].text)
            "Bonjour, le monde!"
        """
        model = self._get_model(request_type)
        prompt = self._format_prompt(request_type, input_text, **kwargs)
        
        llm_request = LLMRequest(
            prompt=prompt,
            model=model.model_name,
            max_tokens=kwargs.get('max_tokens', 100),
            temperature=kwargs.get('temperature', 0.7)
        )
        
        generated_text = await model.generate(
            prompt=llm_request.prompt,
            max_tokens=llm_request.max_tokens,
            temperature=llm_request.temperature
        )
        
        return LLMResponse(
            id=f"response-{hash(generated_text)}",
            object="text_completion",
            created=int(time.time()),
            model=model.model_name,
            choices=[{"text": generated_text, "index": 0, "logprobs": None, "finish_reason": "length"}],
            usage={"prompt_tokens": len(prompt.split()), "completion_tokens": len(generated_text.split()), "total_tokens": len(prompt.split()) + len(generated_text.split())}
        )

    def _get_model(self, request_type: str) -> Any:
        """
        Get an appropriate model for a given request type.

        This method selects the most suitable model based on the request type.
        It can be extended to implement more complex model selection logic.

        Args:
            request_type (str): The type of request.

        Returns:
            Any: An instance of a model suitable for the request type.

        Raises:
            ValueError: If no suitable model is found for the request type.
        """
        # This is a simplified version. In a real-world scenario, you might have
        # more complex logic to select the appropriate model.
        if request_type in ["translate", "summarize"]:
            return self.model_factory.get_model("gpt-3.5-turbo")
        elif request_type in ["code_generation", "complex_reasoning"]:
            return self.model_factory.get_model("gpt-4")
        else:
            raise ValueError(f"Unsupported request type: {request_type}")

    def _format_prompt(self, request_type: str, input_text: str, **kwargs) -> str:
        """
        Retrieve and format a prompt for a given request type.

        This method gets the appropriate prompt template from the repository
        and formats it with the input text and any additional parameters.

        Args:
            request_type (str): The type of request.
            input_text (str): The input text to be processed.
            **kwargs: Additional parameters for formatting the prompt.

        Returns:
            str: The formatted prompt ready to be sent to the model.

        Raises:
            ValueError: If no suitable prompt template is found for the request type.
        """
        prompt_template = self.prompt_repo.get_prompt(request_type)
        if prompt_template is None:
            raise ValueError(f"No prompt template found for request type: {request_type}")
        
        return prompt_template.format(input_text=input_text, **kwargs)