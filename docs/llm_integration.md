# LLM Integration Guide

## Overview

This guide provides detailed information on integrating and working with Large Language Models (LLMs) in our microservice architecture. It covers LLM provider integration, prompt management, and best practices for effective LLM utilization.

## LLM Provider Integration

### Supported Providers

The microservice currently supports the following LLM providers:

1. OpenAI (GPT-3, GPT-4)
2. Anthropic (Claude)
3. Hugging Face Transformers

### Adding a New Provider

To add support for a new LLM provider:

1. Create a new class in `src/infrastructure/llm_providers/` that extends the base `LLMProvider` class.
2. Implement the required methods: `generate_text()`, `complete_text()`, etc.
3. Add provider-specific error handling.
4. Update the `LLMOrchestrator` in `src/application/services/llm_orchestrator.py` to include the new provider.

Example:

```python
# src/infrastructure/llm_providers/new_provider.py

from .base import LLMProvider

class NewProvider(LLMProvider):
    def __init__(self, api_key: str):
        self.client = NewProviderClient(api_key)

    async def generate_text(self, prompt: str, max_tokens: int, temperature: float) -> str:
        try:
            response = await self.client.generate(prompt, max_tokens=max_tokens, temperature=temperature)
            return response.text
        except NewProviderError as e:
            raise LLMProviderError(str(e))
```

## Prompt Management

### Prompt Templates

Prompt templates are managed in the `src/application/prompt_management/` directory.

To create a new prompt template:

1. Define the template in `prompt_templates.py`.
2. Use the `PromptTemplate` class to create a new template instance.

Example:

```python
# src/application/prompt_management/prompt_templates.py

from .prompt_template import PromptTemplate

SENTIMENT_ANALYSIS_TEMPLATE = PromptTemplate(
    name="sentiment_analysis",
    template="Analyze the sentiment of the following text: {text}\nSentiment:",
    version="1.0"
)
```

### Using Prompts

To use a prompt in your application:

1. Retrieve the prompt template using the `PromptRepository`.
2. Format the prompt with the required parameters.
3. Pass the formatted prompt to the LLM provider.

Example:

```python
# src/application/services/sentiment_service.py

from ..prompt_management.prompt_repository import PromptRepository

async def analyze_sentiment(text: str) -> str:
    prompt_repo = PromptRepository()
    prompt_template = prompt_repo.get_template("sentiment_analysis")
    formatted_prompt = prompt_template.format(text=text)
    
    llm_orchestrator = LLMOrchestrator()
    result = await llm_orchestrator.generate_text(formatted_prompt, max_tokens=50)
    return result
```

## Best Practices

1. **Prompt Engineering**
   - Keep prompts clear and concise.
   - Use examples in prompts for better results.
   - Iterate and refine prompts based on model outputs.

2. **Error Handling**
   - Implement robust error handling for API failures.
   - Use exponential backoff for retries on transient errors.

3. **Performance Optimization**
   - Utilize caching for frequently used prompts and responses.
   - Implement request batching when appropriate.

4. **Cost Management**
   - Monitor token usage to control costs.
   - Use the smallest model that meets your needs.

5. **Security**
   - Never expose API keys in code or logs.
   - Implement input sanitization to prevent prompt injection attacks.

6. **Testing**
   - Create a suite of test prompts for regression testing.
   - Use mocking for LLM responses in unit tests.

7. **Versioning**
   - Version your prompts to track changes over time.
   - Consider versioning your API endpoints for major LLM integrations changes.

By following these guidelines and best practices, you can effectively integrate and utilize LLMs in your microservice architecture, ensuring scalability, maintainability, and optimal performance.