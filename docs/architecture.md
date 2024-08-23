# Architecture Documentation

## Overview

This document outlines the high-level architecture of our LLM-Powered Microservice. The architecture follows Clean Architecture principles and is designed to be scalable, maintainable, and loosely coupled.

## Architectural Principles

1. **Separation of Concerns:** The application is divided into distinct layers, each with a specific responsibility.
2. **Dependency Rule:** Dependencies point inwards. Inner layers are unaware of outer layers.
3. **Abstraction:** Use of interfaces and abstract classes to define boundaries between layers.
4. **Testability:** The architecture facilitates easy testing of business logic independent of external concerns.

## Layers

### 1. Domain Layer (`src/domain/`)

- Contains enterprise-wide business rules and entities.
- Key components:
  - `llm_request.py`: Represents an LLM request entity.
  - `llm_response.py`: Represents an LLM response entity.

### 2. Application Layer (`src/application/`)

- Contains application-specific business rules.
- Orchestrates the flow of data to and from the domain entities.
- Key components:
  - `prompt_management/`: Manages prompt templates and versioning.
  - `services/`: Contains application services like `llm_orchestrator.py`.

### 3. Infrastructure Layer (`src/infrastructure/`)

- Contains implementations of interfaces defined in the application layer.
- Manages all external concerns (databases, external APIs, etc.).
- Key components:
  - `llm_providers/`: Implementations for different LLM providers.
  - `cache/`: Caching mechanisms implementation.

### 4. Presentation Layer (`src/presentation/`)

- Handles HTTP requests and responses.
- Contains API routes and controllers.
- Key components:
  - `api/routes/`: FastAPI route definitions.
  - `api/schemas/`: Pydantic models for request/response validation.

### 5. Core (`src/core/`)

- Contains cross-cutting concerns and shared utilities.
- Key components:
  - `config.py`: Configuration management.
  - `exceptions.py`: Custom exception classes.
  - `logging.py`: Logging configuration.

## Key Components

### LLM Orchestrator

- Located in `src/application/services/llm_orchestrator.py`.
- Manages interactions with LLM providers.
- Handles model selection, request routing, and response processing.

### Prompt Management

- Located in `src/application/prompt_management/`.
- Manages prompt templates and versioning.
- Provides an interface for creating and retrieving prompts.

### Caching Layer

- Implemented in `src/infrastructure/cache/`.
- Provides caching mechanisms to improve performance and reduce API costs.

### LLM Providers

- Located in `src/infrastructure/llm_providers/`.
- Abstract base class and concrete implementations for different LLM providers.
- Handles API communication and error handling specific to each provider.

## Data Flow

1. HTTP request received by FastAPI application.
2. Request routed to appropriate endpoint in `src/presentation/api/routes/`.
3. Request data validated using Pydantic models.
4. Application service (e.g., LLM Orchestrator) processes the request.
5. If needed, data is retrieved or stored using infrastructure layer components.
6. LLM provider is called to generate response.
7. Response is processed and returned through the API.

## Error Handling

- Custom exceptions defined in `src/core/exceptions.py`.
- Global exception handler to ensure consistent error responses.
- LLM-specific error handling in provider implementations.

## Configuration Management

- Environment-based configuration using `python-dotenv`.
- Configuration parameters defined in `src/core/config.py`.
- Sensitive data (API keys, etc.) managed through environment variables.

## Scalability Considerations

- Stateless design to allow horizontal scaling.
- Use of caching to reduce load on LLM APIs.
- Asynchronous processing of LLM requests.

## Testing Strategy

- Unit tests for individual components.
- Integration tests for testing interactions between components.
- Mocking of LLM provider responses for consistent testing.

This architecture provides a solid foundation for building scalable and maintainable LLM-powered microservices. It separates concerns, allows for easy testing, and provides flexibility in integrating different LLM providers.