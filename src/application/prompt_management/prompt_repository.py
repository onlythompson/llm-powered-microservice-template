from pydantic import BaseModel, Field
from typing import Dict, Any
from string import Template

class PromptTemplate(BaseModel):
    """
    A class representing a template for prompts used with Language Models (LLMs).

    This class allows for the creation, versioning, and formatting of prompt templates.
    It uses Python's string.Template for variable substitution in the prompt.

    Attributes:
        name (str): The name of the prompt template.
        template (str): The actual template string with placeholders for variables.
        version (str): The version of the prompt template. Defaults to "1.0".
        description (str): A brief description of the prompt template's purpose or usage.
        metadata (Dict[str, Any]): Additional metadata associated with the template.

    Methods:
        format: Fills in the template with provided variables.
        get_required_variables: Returns a set of variable names required by the template.

    Example:
        >>> template = PromptTemplate(
        ...     name="greeting",
        ...     template="Hello, {name}! Welcome to {place}.",
        ...     description="A simple greeting template"
        ... )
        >>> template.format(name="Alice", place="Wonderland")
        'Hello, Alice! Welcome to Wonderland.'
    """

    name: str
    template: str
    version: str = "1.0"
    description: str = ""
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def format(self, **kwargs) -> str:
        """
        Format the prompt template with the given arguments.

        This method uses a safe string substitution to fill in the template
        with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments corresponding to the placeholders in the template.

        Returns:
            str: The formatted prompt string.

        Raises:
            KeyError: If a required placeholder is not provided in kwargs.

        Example:
            >>> template = PromptTemplate(name="example", template="Hello, {name}!")
            >>> template.format(name="World")
            'Hello, World!'
        """
        template = Template(self.template)
        return template.safe_substitute(**kwargs)

    def get_required_variables(self) -> set:
        """
        Return a set of variable names required by this template.

        This method analyzes the template string and returns a set of all
        placeholder names that need to be filled for a complete prompt.

        Returns:
            set: A set of strings representing the required variable names.

        Example:
            >>> template = PromptTemplate(name="example", template="Hello, {name}! Welcome to {place}.")
            >>> template.get_required_variables()
            {'name', 'place'}
        """
        return set(Template(self.template).get_identifiers())