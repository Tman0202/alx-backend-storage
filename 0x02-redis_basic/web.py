#!/usr/bin/env python3
""" Web advanced task """

import requests
import redis
from functools import wraps
from typing import Callable

db = redis.Redis()


def url_access_counter(funct: Callable) -> Callable:
    """ Decorator counting number of times
    a URL is accessed """

    @wraps(funct)
    def wrapper(url):
        db_cache_key = "cached:" + url
        counter_key = "count:" + url
        db.incr(counter_key)
        cached_data = db.get(db_cache_key)
        if cached_data:
            return cached_data.decode("utf-8")

        html_file = funct(url)
        db.setex(db_cache_key, 10, html_file)
        return html_file

    return wrapper


@url_access_counter
def get_page(url: str) -> str:
    """ Returns the HTML content in a url """
    content = requests.get(url)
    return content.text
