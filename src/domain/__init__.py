"""
Domain Module

This module defines the core domain entities for the LLM-powered microservice.
It includes the fundamental data structures that represent LLM requests and responses.

Components:
- LLMRequest: Represents a request to a Language Model (LLM)
- LLMResponse: Represents a response from a Language Model (LLM)

Usage:
    from domain import LLMRequest, LLMResponse

    # Create a new LLM request
    request = LLMRequest(prompt="Translate 'Hello' to French", model="gpt-3.5-turbo", max_tokens=50)

    # Create a new LLM response
    response = LLMResponse(
        id="response-123",
        choices=[{"text": "Bonjour", "index": 0}],
        usage={"total_tokens": 2}
    )
"""

from .llm_request import LLMRequest
from .llm_response import LLMResponse

__all__ = ["LLMRequest", "LLMResponse"]

# Version of the domain module
__version__ = "0.1.0"