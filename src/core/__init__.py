"""
Core Module

This module contains core components of the LLM-powered microservice,
including configuration management and custom exceptions.

Components:
- config: Application configuration management
- exceptions: Custom exception classes for the application

Usage:
    from core.config import settings
    from core.exceptions import LLMServiceException

    # Access configuration
    api_key = settings.OPENAI_API_KEY

    # Raise a custom exception
    raise LLMServiceException("An error occurred in the LLM service")
"""

from .config import settings
from .exceptions import LLMServiceException

__all__ = ["settings", "LLMServiceException"]

# Version of the core module
__version__ = "0.1.0"