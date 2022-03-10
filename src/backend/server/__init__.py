import fastapi


api = fastapi.FastAPI()


@api.get('/hello_world')
async def root():
    return {
        "message": "Hello World"
    }
