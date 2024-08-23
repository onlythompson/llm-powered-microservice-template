from typing import Dict, Type
from .base_model import BaseModel

class ModelFactory:
    """
    A factory class for creating instances of specific language models.

    This class manages the creation of different language model instances,
    allowing for easy switching between different model implementations.

    Attributes:
        _models (Dict[str, Type[BaseModel]]): A dictionary mapping model names to their respective classes.

    Methods:
        register_model: Register a new model class with the factory.
        get_model: Get an instance of a specific model.
        list_available_models: List all available model names.
    """

    def __init__(self):
        self._models: Dict[str, Type[BaseModel]] = {}

    def register_model(self, model_name: str, model_class: Type[BaseModel]):
        """
        Register a new model class with the factory.

        Args:
            model_name (str): The name of the model.
            model_class (Type[BaseModel]): The class of the model to register.

        Example:
            >>> factory = ModelFactory()
            >>> factory.register_model("gpt-3.5-turbo", GPT35TurboModel)
        """
        self._models[model_name] = model_class

    def get_model(self, model_name: str) -> BaseModel:
        """
        Get an instance of a specific model.

        Args:
            model_name (str): The name of the model to instantiate.

        Returns:
            BaseModel: An instance of the requested model.

        Raises:
            ValueError: If the requested model is not registered with the factory.

        Example:
            >>> factory = ModelFactory()
            >>> factory.register_model("gpt-3.5-turbo", GPT35TurboModel)
            >>> model = factory.get_model("gpt-3.5-turbo")
        """
        model_class = self._models.get(model_name)
        if model_class is None:
            raise ValueError(f"Model '{model_name}' is not registered with the factory")
        return model_class(model_name)

    def list_available_models(self) -> list[str]:
        """
        List all available model names.

        Returns:
            list[str]: A list of all registered model names.

        Example:
            >>> factory = ModelFactory()
            >>> factory.register_model("gpt-3.5-turbo", GPT35TurboModel)
            >>> factory.register_model("gpt-4", GPT4Model)
            >>> factory.list_available_models()
            ['gpt-3.5-turbo', 'gpt-4']
        """
        return list(self._models.keys())