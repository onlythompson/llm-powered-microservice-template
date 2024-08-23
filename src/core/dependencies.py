from fastapi import Depends
from functools import lru_cache
from typing import Generator

from application.services.llm_orchestrator import LLMOrchestrator
from infrastructure.cache.redis_cache import RedisCache
from infrastructure.llm_providers.openai import OpenAIProvider
from infrastructure.llm_providers.anthropic import AnthropicProvider
from application.models.model_factory import ModelFactory
from application.prompt_management.prompt_repository import PromptRepository
from .config import settings

@lru_cache()
def get_redis_cache() -> RedisCache:
    return RedisCache(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )

@lru_cache()
def get_model_factory() -> ModelFactory:
    factory = ModelFactory()
    factory.register_model("gpt-3.5-turbo", OpenAIProvider(settings.OPENAI_API_KEY))
    factory.register_model("claude-v1", AnthropicProvider(settings.ANTHROPIC_API_KEY))
    return factory

@lru_cache()
def get_prompt_repository() -> PromptRepository:
    return PromptRepository()

@lru_cache()
def get_llm_orchestrator(
    cache: RedisCache = Depends(get_redis_cache),
    model_factory: ModelFactory = Depends(get_model_factory),
    prompt_repo: PromptRepository = Depends(get_prompt_repository)
) -> LLMOrchestrator:
    return LLMOrchestrator(model_factory, prompt_repo, cache)

def get_db() -> Generator:
    # This is a placeholder for database session management
    # You would typically set up and yield a database session here
    db = None
    try:
        yield db
    finally:
        # Close the database session
        pass