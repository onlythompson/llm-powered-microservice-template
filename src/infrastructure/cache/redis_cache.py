import json
from typing import Any, Optional
import aioredis

class RedisCache:
    """
    A Redis-based caching implementation.

    This class provides methods to interact with a Redis cache, allowing for
    storing, retrieving, and deleting cached items. It uses aioredis for
    asynchronous Redis operations.

    Attributes:
        redis (aioredis.Redis): The Redis client instance.

    Methods:
        set: Store a value in the cache.
        get: Retrieve a value from the cache.
        delete: Remove a value from the cache.
        flush: Clear all items from the cache.
    """

    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        """
        Initialize the RedisCache.

        Args:
            host (str): The Redis server host. Defaults to 'localhost'.
            port (int): The Redis server port. Defaults to 6379.
            db (int): The Redis database number. Defaults to 0.
        """
        self.redis = aioredis.from_url(f"redis://{host}:{port}/{db}")

    async def set(self, key: str, value: Any, expire: int = None) -> None:
        """
        Store a value in the cache.

        Args:
            key (str): The key under which to store the value.
            value (Any): The value to store. Will be JSON-encoded.
            expire (int, optional): Time in seconds after which the key will expire.
                                    If None, the key will not expire.

        Raises:
            ValueError: If the value cannot be JSON encoded.
        """
        try:
            json_value = json.dumps(value)
            await self.redis.set(key, json_value, ex=expire)
        except TypeError as e:
            raise ValueError(f"Unable to JSON encode the value: {e}")

    async def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            Optional[Any]: The retrieved value, or None if the key doesn't exist.
                           The value is JSON-decoded before being returned.

        Raises:
            ValueError: If the stored value cannot be JSON decoded.
        """
        value = await self.redis.get(key)
        if value is None:
            return None
        try:
            return json.loads(value)
        except json.JSONDecodeError as e:
            raise ValueError(f"Unable to JSON decode the stored value: {e}")

    async def delete(self, key: str) -> None:
        """
        Remove a value from the cache.

        Args:
            key (str): The key of the value to remove.
        """
        await self.redis.delete(key)

    async def flush(self) -> None:
        """
        Clear all items from the cache.

        Warning: This will remove all keys from the current database.
        """
        await self.redis.flushdb()

    async def close(self) -> None:
        """
        Close the Redis connection.

        This method should be called when the cache is no longer needed.
        """
        await self.redis.close()