# LLM-Powered Microservice Template

## Overview

This repository provides a template for building Large Language Model (LLM) powered microservices using FastAPI. It's designed to help you quickly set up and deploy AI-driven APIs that leverage the power of LLMs like GPT-3, GPT-4, Claude or other similar models.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Quick Start](#quick-start)
5. [Project Structure](#project-structure)
6. [Configuration](#configuration)
7. [Usage Examples](#usage-examples)
   - [LLM Orchestrator](#llm-orchestrator)
   - [Prompt Management](#prompt-management)
   - [Caching](#caching)
8. [API Endpoints](#api-endpoints)
9. [Components](#components)
   - [LLM Providers](#llm-providers)
   - [Chains](#chains)
   - [Cross-Cutting Concerns](#cross-cutting-concerns)
10. [Testing](#testing)
11. [Deployment](#deployment)
    - [Docker](#docker)
    - [Kubernetes](#kubernetes)
12. [Documentation](#documentation)
13. [Contributing](#contributing)
14. [License](#license)
15. [Acknowledgments](#acknowledgments)

## Features

- 🚀 FastAPI framework for high-performance API development
- 🏗️ Clean Architecture principles for maintainable and scalable code
- 🔌 LLM integration with support for multiple providers (e.g., OpenAI, Anthropic)
- 📝 Prompt management system for versioning and reusing prompts
- ⚡ Asynchronous processing of LLM requests
- 💾 Caching layer for improved performance and reduced API costs
- 🛠️ Comprehensive error handling and logging
- 🕸️ Distributed tracing with OpenTelemetry and Jaeger
- 💉 Dependency Injection for improved testability and maintainability
- 🐳 Dockerized setup for easy deployment
- ☸️ Kubernetes configuration for scalable cloud deployments

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Kubernetes (for production deployment)

## Quick Start

1. Use this template to create a new GitHub repository.
2. Clone your new repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
3. Run the directory structure generation script:
   ```bash
   python scripts/create_structure.py
   ```
4. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your LLM API keys and other configuration.
7. Run the development server:
   ```bash
   uvicorn src.main:app --reload
   ```

Visit `http://localhost:8000/docs` to see the API documentation.

## Project Structure

```
my_fastapi_microservice/
├── src/
│   ├── application/
│   │   ├── chains/
│   │   ├── models/
│   │   ├── prompt_management/
│   │   └── services/
│   ├── core/
│   ├── domain/
│   ├── infrastructure/
│   │   ├── cache/
│   │   └── llm_providers/
│   └── presentation/
│       └── api/
│           ├── routes/
│           └── schemas/
├── tests/
├── docs/
├── k8s/
└── scripts/
    └── create_structure.py
```

## Configuration

LLM-specific configurations are managed in `src/core/config.py`. You can specify:

- LLM provider settings
- Model selection
- Token limits
- Caching parameters

## Testing

Run the test suite with:

```
pytest
```
## Documentation

Detailed documentation for various aspects of this project can be found in the `/docs` directory:

1. [API Documentation](docs/api.md)
   - Comprehensive guide to the APIs exposed by the microservice
   - Includes endpoints, request/response formats, authentication, and error handling

2. [Architecture Documentation](docs/architecture.md)
   - Overview of the high-level architecture following Clean Architecture principles
   - Describes layers, key components, data flow, and scalability considerations

3. [Deployment Guide](docs/deployment.md)
   - Instructions for deploying the microservice using Docker and Kubernetes
   - Includes scaling, monitoring, and troubleshooting information

4. [LLM Integration Guide](docs/llm_integration.md)
   - Details on integrating and working with Large Language Models
   - Covers LLM provider integration, prompt management, and best practices

5. [Security Documentation](docs/security.md)
   - Outlines security measures and best practices implemented in the microservice
   - Includes authentication, authorization, data protection, and LLM-specific security considerations

Please refer to these documents for in-depth information on specific topics related to the project.


## Usage

Here are some examples of how to use different components of the microservice:

### LLM Orchestrator

The LLM Orchestrator manages interactions with different LLM providers. Here's how to use it:

```python
from application.services.llm_orchestrator import LLMOrchestrator
from core.dependencies import get_model_factory, get_prompt_repository, get_redis_cache

model_factory = get_model_factory()
prompt_repo = get_prompt_repository()
cache = get_redis_cache()

orchestrator = LLMOrchestrator(model_factory, prompt_repo, cache)

response = await orchestrator.process_request("generate", 
    prompt="Translate the following English text to French: 'Hello, world!'",
    max_tokens=50
)
print(response.choices[0].text)
```

### Prompt Management

The Prompt Management system allows you to create, store, and retrieve prompt templates:

```python
from application.prompt_management.prompt_template import PromptTemplate
from application.prompt_management.prompt_repository import PromptRepository

repo = PromptRepository()

# Create a new prompt template
translation_prompt = PromptTemplate(
    name="translation",
    template="Translate the following {source_language} text to {target_language}: {text}",
    version="1.0"
)

# Add the prompt to the repository
repo.add_prompt(translation_prompt)

# Retrieve and use the prompt
prompt = repo.get_prompt("translation")
formatted_prompt = prompt.format(
    source_language="English",
    target_language="French",
    text="Hello, world!"
)
print(formatted_prompt)
```

### Caching

The Redis-based caching system can be used to store and retrieve LLM responses:

```python
from infrastructure.cache.redis_cache import RedisCache

cache = RedisCache(host='localhost', port=6379, db=0)

# Caching a response
await cache.set('llm_response:hello_world', 'Bonjour, le monde!', expire=3600)

# Retrieving a cached response
cached_response = await cache.get('llm_response:hello_world')
print(cached_response)
```

## API Endpoints

The microservice exposes the following main API endpoints:

- `POST /api/llm/generate`: Generate text using an LLM
- `POST /api/llm/summarize`: Summarize text using an LLM
- `GET /api/llm/models`: List available LLM models

For detailed API documentation, run the server and visit `http://localhost:8000/docs`.

## Components

### LLM Providers

The microservice supports multiple LLM providers. To add a new provider:

1. Create a new file in `src/infrastructure/llm_providers/`
2. Implement the provider class, inheriting from `BaseLLMProvider`
3. Register the new provider in `src/core/dependencies.py`

### Chains

Chains represent sequences of operations involving prompts and language models. To create a new chain:

1. Create a new file in `src/application/chains/specific_chains/`
2. Implement the chain class, inheriting from `BaseChain`
3. Register the new chain in `src/application/chains/__init__.py`

### Cross-Cutting Concerns

Logging, tracing, and other cross-cutting concerns are managed in `src/core/cross_cutting.py`. This includes:

- Logging configuration
- Distributed tracing setup with OpenTelemetry and Jaeger
- Middleware for request/response logging


## Deployment

### Docker

Build and run the Docker container:

```
docker build -t llm-microservice .
docker run -p 8000:8000 llm-microservice
```

### Kubernetes

Apply the Kubernetes manifests:

```
kubectl apply -f k8s/
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI framework
- OpenAI and other LLM providers
- The open-source community

For more detailed information, please refer to the documentation in the `docs/` directory.