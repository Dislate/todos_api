from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {
        "message": "Hello client"
    }


if __name__ == '__main__':
    pass
