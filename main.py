from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/blog")
async def show(req: Request):
    param = req.path_params
    aparams=req.query_params
    return {"data": aparams.get('name')}
