from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def msg():
    return {"msg":"success"}

