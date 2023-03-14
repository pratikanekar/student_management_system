from fastapi import FastAPI
from uvicorn import run
from routes.index import user
from loguru import logger
logger.debug("This is debug")
# logger.info("This is information")
logger.success("this is success")
# logger.warning("this is warning")
app = FastAPI(
    title="Student Management"
)


# @app.get("/")
# async def display():
#     return {"hello":"world"}

app.include_router(user)


if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=12000, reload=True)
