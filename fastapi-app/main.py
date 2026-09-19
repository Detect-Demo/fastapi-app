from fastapi import FastAPI

app = FastAPI(title="fastapi-app demo")


@app.get("/")
def root():
    return {"demo": "fastapi-app", "stack": "python-fastapi"}
