from fastapi import FastAPI
from endpoints.todos import todo_router

app = FastAPI()
app.include_router(todo_router)

@app.get('/')
async def welcome() -> dict:
    return {
        "message": "Hello client"
    }


if __name__ == '__main__':
    pass
