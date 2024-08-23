"""
Cache Module

This module provides caching mechanisms for the LLM-powered microservice.
It includes implementations for different caching strategies, with Redis
being the primary caching solution.

Components:
- RedisCache: A Redis-based caching implementation

Usage:
    from infrastructure.cache import RedisCache

    redis_cache = RedisCache(host='localhost', port=6379, db=0)
    
    # Caching a value
    await redis_cache.set('key', 'value', expire=3600)
    
    # Retrieving a cached value
    value = await redis_cache.get('key')
"""

from .redis_cache import RedisCache

__all__ = ["RedisCache"]

# Version of the cache module
__version__ = "0.1.0"