from typing import Dict, List, Optional
from .prompt_template import PromptTemplate

class PromptRepository:
    """
    A repository for managing and storing PromptTemplate objects.

    This class provides methods for adding, retrieving, updating, and deleting
    prompt templates. It supports versioning of prompts and allows retrieval
    of specific versions or the latest version of a prompt.

    Attributes:
        prompts (Dict[str, PromptTemplate]): A dictionary storing the prompt templates,
            keyed by a string in the format "name:version".

    Methods:
        add_prompt: Add a new prompt template to the repository.
        get_prompt: Retrieve a prompt template by name and optionally version.
        list_prompts: Return a list of all prompt templates in the repository.
        update_prompt: Update an existing prompt template.
        delete_prompt: Delete a prompt template from the repository.

    Example:
        >>> repo = PromptRepository()
        >>> template = PromptTemplate(name="greeting", template="Hello, {name}!", version="1.0")
        >>> repo.add_prompt(template)
        >>> retrieved = repo.get_prompt("greeting")
        >>> retrieved.format(name="World")
        'Hello, World!'
    """

    def __init__(self):
        self.prompts: Dict[str, PromptTemplate] = {}

    def add_prompt(self, prompt: PromptTemplate) -> None:
        """
        Add a new prompt template to the repository.

        Args:
            prompt (PromptTemplate): The prompt template to add.

        Raises:
            ValueError: If a prompt with the same name and version already exists.

        Example:
            >>> repo = PromptRepository()
            >>> template = PromptTemplate(name="example", template="Hello, {name}!", version="1.0")
            >>> repo.add_prompt(template)
        """
        key = f"{prompt.name}:{prompt.version}"
        if key in self.prompts:
            raise ValueError(f"Prompt '{key}' already exists in repository")
        self.prompts[key] = prompt

    def get_prompt(self, name: str, version: Optional[str] = None) -> Optional[PromptTemplate]:
        """
        Retrieve a prompt template by name and optionally version.

        If version is not specified, returns the latest version of the prompt.

        Args:
            name (str): The name of the prompt template to retrieve.
            version (Optional[str]): The version of the prompt template. If None,
                the latest version is returned.

        Returns:
            Optional[PromptTemplate]: The requested prompt template, or None if not found.

        Example:
            >>> repo = PromptRepository()
            >>> template = PromptTemplate(name="example", template="Hello, {name}!", version="1.0")
            >>> repo.add_prompt(template)
            >>> retrieved = repo.get_prompt("example")
            >>> retrieved.version
            '1.0'
        """
        if version:
            key = f"{name}:{version}"
            return self.prompts.get(key)
        
        # If version is not specified, find the latest version
        matching_prompts = [p for k, p in self.prompts.items() if k.startswith(f"{name}:")]
        if not matching_prompts:
            return None
        return max(matching_prompts, key=lambda p: p.version)

    def list_prompts(self) -> List[PromptTemplate]:
        """
        Return a list of all prompt templates in the repository.

        Returns:
            List[PromptTemplate]: A list of all stored prompt templates.

        Example:
            >>> repo = PromptRepository()
            >>> template1 = PromptTemplate(name="example1", template="Hello, {name}!", version="1.0")
            >>> template2 = PromptTemplate(name="example2", template="Goodbye, {name}!", version="1.0")
            >>> repo.add_prompt(template1)
            >>> repo.add_prompt(template2)
            >>> len(repo.list_prompts())
            2
        """
        return list(self.prompts.values())

    def update_prompt(self, prompt: PromptTemplate) -> None:
        """
        Update an existing prompt template.

        Args:
            prompt (PromptTemplate): The updated prompt template.

        Raises:
            KeyError: If the prompt with the given name and version doesn't exist.

        Example:
            >>> repo = PromptRepository()
            >>> template = PromptTemplate(name="example", template="Hello, {name}!", version="1.0")
            >>> repo.add_prompt(template)
            >>> updated = PromptTemplate(name="example", template="Hi, {name}!", version="1.0")
            >>> repo.update_prompt(updated)
            >>> repo.get_prompt("example").template
            'Hi, {name}!'
        """
        key = f"{prompt.name}:{prompt.version}"
        if key not in self.prompts:
            raise KeyError(f"Prompt '{key}' not found in repository")
        self.prompts[key] = prompt

    def delete_prompt(self, name: str, version: str) -> None:
        """
        Delete a prompt template from the repository.

        Args:
            name (str): The name of the prompt template to delete.
            version (str): The version of the prompt template to delete.

        Raises:
            KeyError: If the prompt with the given name and version doesn't exist.

        Example:
            >>> repo = PromptRepository()
            >>> template = PromptTemplate(name="example", template="Hello, {name}!", version="1.0")
            >>> repo.add_prompt(template)
            >>> repo.delete_prompt("example", "1.0")
            >>> repo.get_prompt("example") is None
            True
        """
        key = f"{name}:{version}"
        if key not in self.prompts:
            raise KeyError(f"Prompt '{key}' not found in repository")
        del self.prompts[key]