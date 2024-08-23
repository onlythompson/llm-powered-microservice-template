"""
API Routes Module

This module contains the route definitions for the LLM-powered microservice API.
It includes routes for various LLM-related operations such as text generation,
summarization, and other NLP tasks.

Components:
- llm_router: Router containing all LLM-related API endpoints

Usage:
    from fastapi import FastAPI
    from presentation.api.routes import llm_router

    app = FastAPI()
    app.include_router(llm_router, prefix="/api/llm", tags=["LLM"])
"""

from .llm_routes import router as llm_router

__all__ = ["llm_router"]

# Version of the routes module
__version__ = "0.1.0"