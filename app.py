import asyncio

from fastapi import FastAPI
from function.example_function import example_functiion

app = FastAPI(docs_url="docs")


@app.get("/")
async def read_root():
    return "GKE service is working!"


@app.post(page="/example", tags="example")
async def example():
    await asyncio.to_thread(thread_example())
    return "Example!"


def thread_example():
    example_functiion()
