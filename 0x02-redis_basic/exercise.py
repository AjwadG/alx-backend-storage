#!/usr/bin/env python3
"""
exercise.py
"""
from typing import Union
import redis
import uuid


class Cache:
    """
    Cache class.

    This class is a wrapper around the Redis cache database.
    It provides a simple interface to store and retrieve data
    from the cache.
    """

    def __init__(self) -> None:
        """
        Initializes the cache class by creating a new Redis connection
        and removing any data in the db.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Saves the data in to the Redis db and returns
        the key to the value.

        Parameters:
            data: The data to be stored in the cache.

        Returns:
            The key to the value stored in the cache.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
