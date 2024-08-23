"""
LLM Providers Module

This module contains implementations for various Language Model (LLM) providers.
It includes a base class that defines the interface for all LLM providers,
as well as specific implementations for different providers like OpenAI and Anthropic.

Components:
- BaseLLMProvider: Abstract base class for all LLM providers
- OpenAIProvider: Implementation for OpenAI's GPT models
- AnthropicProvider: Implementation for Anthropic's Claude models

Usage:
    from infrastructure.llm_providers import OpenAIProvider, AnthropicProvider

    openai_provider = OpenAIProvider(api_key="your-openai-api-key")
    anthropic_provider = AnthropicProvider(api_key="your-anthropic-api-key")

    response = await openai_provider.generate_text("Translate 'Hello' to French")
    print(response)
"""

from .base import BaseLLMProvider
from .openai import OpenAIProvider
from .anthropic import AnthropicProvider

__all__ = ["BaseLLMProvider", "OpenAIProvider", "AnthropicProvider"]

# Version of the LLM providers module
__version__ = "0.1.0"