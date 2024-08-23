"""
Prompt Management Module

This module provides tools for creating, storing, and managing prompt templates
for use with Language Models (LLMs) in the LLM-powered microservice.

Components:
- PromptTemplate: A class for creating and formatting prompt templates
- PromptRepository: A class for storing and retrieving prompt templates

Usage:
    from application.prompt_management import PromptTemplate, PromptRepository

    # Create a new prompt template
    greeting_prompt = PromptTemplate(
        name="greeting",
        template="Hello, {name}! Welcome to {place}.",
        version="1.0"
    )

    # Create a prompt repository
    repo = PromptRepository()

    # Add the prompt to the repository
    repo.add_prompt(greeting_prompt)

    # Retrieve and use the prompt
    retrieved_prompt = repo.get_prompt("greeting")
    formatted_prompt = retrieved_prompt.format(name="Alice", place="Wonderland")
"""

from .prompt_template import PromptTemplate
from .prompt_repository import PromptRepository

__all__ = ["PromptTemplate", "PromptRepository"]

# Version of the prompt management module
__version__ = "0.1.0"