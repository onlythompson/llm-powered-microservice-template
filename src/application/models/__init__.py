"""
Models Module

This module provides abstractions and factories for working with different Language Model (LLM) providers.
It includes a base model class and a factory for creating specific model instances.

Components:
- BaseModel: An abstract base class for all language models
- ModelFactory: A factory class for creating instances of specific language models

Usage:
    from application.models import BaseModel, ModelFactory

    # Create a model factory
    factory = ModelFactory()

    # Get a specific model instance
    model = factory.get_model("gpt-3.5-turbo")

    # Use the model
    response = await model.generate("Hello, world!")
"""

from .base_model import BaseModel
from .model_factory import ModelFactory

__all__ = ["BaseModel", "ModelFactory"]

# Version of the models module
__version__ = "0.1.0"