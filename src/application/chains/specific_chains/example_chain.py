from ..base_chain import BaseChain
from ...prompts.prompt_repository import PromptRepository
from ...models.model_factory import ModelFactory
from typing import Any, Dict

class ExampleChain(BaseChain):
    """
    An example implementation of a chain for demonstration purposes.
    
    This chain takes a user query, processes it through a language model,
    and returns a response.
    """

    def __init__(self, prompt_repo: PromptRepository, model_factory: ModelFactory):
        self.prompt_repo = prompt_repo
        self.model_factory = model_factory

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the example chain.

        Args:
            inputs (Dict[str, Any]): Should contain a 'query' key with the user's input.

        Returns:
            Dict[str, Any]: Contains a 'response' key with the model's output.
        """
        query = inputs['query']
        prompt_template = self.prompt_repo.get_prompt("example_prompt")
        formatted_prompt = prompt_template.format(query=query)

        model = self.model_factory.get_model("gpt-3.5-turbo")
        response = await model.generate(formatted_prompt)

        return {"response": response}

    def get_input_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }

    def get_output_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "response": {"type": "string"}
            },
            "required": ["response"]
        }