#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis for storing,
retrieving, and tracking data, as well as decorators for counting method calls
and recording call history.
"""

import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of calls to a method.
    Args:
        method (Callable): The method to be wrapped.
    Returns:
        Callable: The wrapped method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function.
    Args:
        method (Callable): The method to be wrapped.
    Returns:
        Callable: The wrapped method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    """
    A Cache class for storing and retrieving data in a Redis database.
    """

    def __init__(self):
        """
        Initialize the Cache instance, connecting to Redis and flushing the
        database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis cache with a randomly generated key.
        Args:
            data (Union[str, bytes, int, float]): The data to be stored in
            the cache.
        Returns:
            str: The randomly generated key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.
        Args:
            key (str): The key to look up in Redis.
            fn (Optional[Callable]): A function to convert the data to the
            desired format.
        Returns:
            Union[str, bytes, int, float, None]: The retrieved data,
            optionally transformed by fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and convert it to a UTF-8 string.
        Args:
            key (str): The key to look up in Redis.
        Returns:
            Optional[str]: The retrieved string data, or None if the key
            doesn't exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.
        Args:
            key (str): The key to look up in Redis.
        Returns:
            Optional[int]: The retrieved integer data, or None if the key
            doesn't exist.
        """
        return self.get(key, fn=int)


def replay(method: Callable):
    """
    Display the history of calls of a particular function.
    Args:
        method (Callable): The method whose history to display.
    """
    cache = method.__self__
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        input_data = input_data.decode('utf-8')
        output_data = output_data.decode('utf-8')
        print(f"{method_name}(*{input_data}) -> {output_data}")
