# Contributing to LLM-Powered Microservice

First off, thank you for considering contributing to our LLM-Powered Microservice template! It's people like you that make this project such a great tool for the community.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How Can I Contribute?](#how-can-i-contribute)
4. [Style Guidelines](#style-guidelines)
5. [LLM-Specific Guidelines](#llm-specific-guidelines)
6. [Commit Messages](#commit-messages)
7. [Pull Requests](#pull-requests)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to codewiththompson@gmail.com.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally.
3. Set up your environment as described in the README.md.
4. Create a branch for your changes.

## How Can I Contribute?

### Reporting Bugs

- Use a clear and descriptive title.
- Describe the exact steps which reproduce the problem.
- Provide specific examples to demonstrate the steps.

### Suggesting Enhancements

- Use a clear and descriptive title.
- Provide a step-by-step description of the suggested enhancement.
- Explain why this enhancement would be useful to most users.

### Your First Code Contribution

- Look for issues labeled "good first issue" or "help wanted".
- Ask for help if you need it!

## Style Guidelines

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
- Use type hints for function arguments and return values.
- Write docstrings for all public modules, functions, classes, and methods.

### Tools

We use the following tools to enforce coding standards:

- `black` for code formatting
- `isort` for import sorting
- `flake8` for linting
- `mypy` for static type checking

Run these before submitting a pull request:

```bash
black .
isort .
flake8
mypy .
```

## LLM-Specific Guidelines

1. **Prompt Management**
   - All prompts should be versioned and stored in the `src/application/prompt_management/` directory.
   - Use the `PromptTemplate` class for creating new prompts.
   - Document the purpose and expected inputs/outputs for each prompt.

2. **LLM Provider Integration**
   - When adding support for a new LLM provider, create a new class in `src/infrastructure/llm_providers/` that extends the base provider class.
   - Ensure all provider-specific logic is encapsulated within its respective class.

3. **Error Handling**
   - Use custom exception classes defined in `src/core/exceptions.py` for LLM-specific errors.
   - Implement appropriate error handling for API rate limits, token limits, and other LLM-specific issues.

4. **Testing LLM Integrations**
   - Write unit tests for all LLM-related functions and classes.
   - Use mocking to simulate LLM API responses in tests.
   - Include integration tests that use a test LLM instance or a simplified model.

5. **Security and Privacy**
   - Never commit API keys or sensitive information.
   - Implement proper sanitization for user inputs that will be sent to LLM APIs.

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Pull Requests

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

Thank you for contributing to the LLM-Powered Microservice project!