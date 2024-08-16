#!/usr/bin/env python3
"""
This module provides a web caching system using Redis.
"""
import redis
import requests
from typing import Callable


def get_page(url: str) -> str:
    """
    Fetch a page and cache its content for 10 seconds.
    Args:
        url (str): The URL of the page to fetch.
    Returns:
        str: The content of the page.
    """
    _redis = redis.Redis()
    cache_key = f"count:{url}"
    _redis.incr(cache_key)

    cached_page = _redis.get(url)
    if cached_page:
        return cached_page.decode('utf-8')

    response = requests.get(url)
    _redis.setex(url, 10, response.text)
    return response.text
