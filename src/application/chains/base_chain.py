from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseChain(ABC):
    """
    Abstract base class for all chains in the application.
    
    A chain represents a sequence of operations to be performed,
    typically involving prompts and language models.
    """

    @abstractmethod
    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the chain with the given inputs.

        Args:
            inputs (Dict[str, Any]): The input parameters for the chain.

        Returns:
            Dict[str, Any]: The output of the chain execution.
        """
        pass

    @abstractmethod
    def get_input_schema(self) -> Dict[str, Any]:
        """
        Get the schema of expected inputs for this chain.

        Returns:
            Dict[str, Any]: A dictionary describing the expected input structure.
        """
        pass

    @abstractmethod
    def get_output_schema(self) -> Dict[str, Any]:
        """
        Get the schema of expected outputs for this chain.

        Returns:
            Dict[str, Any]: A dictionary describing the expected output structure.
        """
        pass