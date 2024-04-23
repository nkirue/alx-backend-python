#!/usr/bin/env python3
'''Coroutine loops 10 times.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Coroutine loops 10 times.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()*10
