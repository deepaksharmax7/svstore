
from fastapi import FastAPI
from mangum import Mangum

from routers import register, deregister, health, search

app = FastAPI()

app.include_router(register.router)
app.include_router(deregister.router)
app.include_router(health.router)
app.include_router(search.router)

# Create a handler for AWS Lambda
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
