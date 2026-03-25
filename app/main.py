from fastapi import FastAPI
from .routers import items

app = FastAPI()

app.include_router(items.router)

@app.get("/")
def read_root():
    return {"Hello": "py World"}



# def main():
#     print("Hello from py-webservice!")


# if __name__ == "__main__":
#     main()
