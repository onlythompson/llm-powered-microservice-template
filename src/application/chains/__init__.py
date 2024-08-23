"""
Chains Module

This module contains implementations of various chains used in the LLM-powered microservice.
Chains represent sequences of operations involving prompts, language models, and potentially other tools or services.

Available Chains:
- BaseChain: The abstract base class for all chains
- ExampleChain: An example implementation of a chain for demonstration purposes

To add a new chain:
1. Create a new file in the `specific_chains` directory
2. Implement your chain class, inheriting from BaseChain
3. Import and add your new chain class to the __all__ list in this file
"""

from .base_chain import BaseChain
from .specific_chains.example_chain import ExampleChain

# Add new chain imports here as they are created
# from .specific_chains.new_chain import NewChain

__all__ = [
    "BaseChain",
    "ExampleChain",
    # Add new chain classes here as they are created
    # "NewChain",
]

# Version of the chains module
__version__ = "0.1.0"