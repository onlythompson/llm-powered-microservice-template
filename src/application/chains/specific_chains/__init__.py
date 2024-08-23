"""
Specific Chains Module

This module contains implementations of specific chains used in the LLM-powered microservice.
Each chain in this module represents a unique sequence of operations designed for a particular use case.

Available Chains:
- ExampleChain: An example implementation of a chain for demonstration purposes

To add a new specific chain:
1. Create a new file in this directory (e.g., new_chain.py)
2. Implement your chain class, inheriting from BaseChain
3. Import your new chain class in this file
4. Add your new chain class to the __all__ list in this file
"""

from .example_chain import ExampleChain

# Add new chain imports here as they are created
# from .new_chain import NewChain

__all__ = [
    "ExampleChain",
    # Add new chain classes here as they are created
    # "NewChain",
]

# Version of the specific chains module
__version__ = "0.1.0"

# You can add any shared utilities or constants for specific chains here
COMMON_CHAIN_CONSTANT = "This is a common constant for all specific chains"

def common_chain_utility():
    """A utility function that can be used across multiple specific chains."""
    return "This is a common utility for all specific chains"