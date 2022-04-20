from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/population")
async def population():
    return requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").json()

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')


