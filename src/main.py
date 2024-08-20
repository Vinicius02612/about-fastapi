from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello Word"}


@app.get("/items/{id_items}")
async def get_item(id_items:int):
    return {"id_items":id_items}
