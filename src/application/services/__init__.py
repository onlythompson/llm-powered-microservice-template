"""
Services Module

This module contains service classes that orchestrate the core functionality
of the LLM-powered microservice. It includes services for managing LLM interactions,
coordinating prompts, and handling complex workflows.

Components:
- LLMOrchestrator: A service for managing interactions with Language Models (LLMs)

Usage:
    from application.services import LLMOrchestrator
    from application.models import ModelFactory
    from application.prompt_management import PromptRepository

    model_factory = ModelFactory()
    prompt_repo = PromptRepository()
    orchestrator = LLMOrchestrator(model_factory, prompt_repo)

    response = await orchestrator.process_request("translate", "Hello, world!", target_language="French")
"""

from .llm_orchestrator import LLMOrchestrator

__all__ = ["LLMOrchestrator"]

# Version of the services module
__version__ = "0.1.0"