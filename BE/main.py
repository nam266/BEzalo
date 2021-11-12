import uvicorn


@app.get("/")
def index():
    return {"Hello": "World"}
