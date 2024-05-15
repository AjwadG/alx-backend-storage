#!/usr/bin/env python3
"""
exercise.py
"""
from typing import Union, Optional, Callable
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

    def get(self, key: str, fn: Optional[Callable] = None) -> bytes:
        """
        Retrieves the data associated with the key from the cache
        and returns it.

        Parameters:
            key: The key associated with the data in the cache.
            fn: A function that can be used to convert the data to
                the desired format. If provided, the data will be
                passed to the function. If not provided, the data
                will be returned as is.

        Returns:
            The data associated with the key in the cache. If a
            conversion function was provided, the converted data
            will be returned. Otherwise, the data will be returned
            as is.
        """
        data: bytes = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves the data associated with the key from the cache
        and returns it as a string.

        Parameters:
            key: The key associated with the data in the cache.

        Returns:
            The data associated with the key in the cache as a
            string.
        """
        return self.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        Retrieves the data associated with the key from the cache
        and returns it as an integer.

        Parameters:
            key: The key associated with the data in the cache.

        Returns:
            The data associated with the key in the cache as an
            integer.
        """
        return int(self.get(key))
