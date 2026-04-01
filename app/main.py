from contextlib import asynccontextmanager
from fastapi import FastAPI
import anyio
from .routers import items

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up with custom lifespan...")
    # 1. Get the current default thread limiter
    limiter = anyio.to_thread.current_default_thread_limiter()
    
    # 2. Print the current size (default is 40)
    print(f"Current thread pool size: {limiter.total_tokens}")
    
    # 3. Update to your new desired size
    limiter.total_tokens = 50
    print(f"New thread pool size: {limiter.total_tokens}")
    
    yield

# app = FastAPI()
app = FastAPI(lifespan=lifespan)

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"Hello": "py World"}



# def main():
#     print("Hello from py-webservice!")


# if __name__ == "__main__":
#     main()
