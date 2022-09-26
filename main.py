import fastapi
import uvicorn

print("hello fastapi")
api = fastapi.FastAPI()

@api.get("/")
def endpoint():
    return {"msg": "Hello everyone", "another msg": ["hello", "world"]}

uvicorn.run(api, port=9000)