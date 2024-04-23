#!/usr/bin/env python3
'''Coroutine async_comprehension that takes no arguments.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Coroutine return 10 random numbers.
    '''
    return [number async for number in async_generator()]
