import asyncio
import random
import os
import time

async def read_file(file_name):
    await asyncio.sleep(random.uniform(0.5, 2))
    return f"Content of {file_name}"

async def read_multiple_files(file_names):
    tasks = []
