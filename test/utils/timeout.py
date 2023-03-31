import asyncio
import functools


class TimeoutException(Exception):
    pass


def timeout(seconds, *, error_message='Timeout'):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            loop = asyncio.get_event_loop()
            task = loop.create_task(func(*args, **kwargs))

            try:
                result = await asyncio.wait_for(task, timeout=seconds)
                return result
            except asyncio.TimeoutError:
                task.cancel()
                raise TimeoutException(error_message)

        return wrapper

    return decorator
