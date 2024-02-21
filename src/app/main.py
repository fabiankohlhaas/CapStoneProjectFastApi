from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI

load_dotenv(find_dotenv())

from app.db_and_models.session import create_db_and_tables, drop_tables
from app.routers.followers import router as follower_router
from app.routers.likes import router as like_router
from app.routers.posts import router as post_router
from app.routers.users import router as user_router

app = FastAPI(
    title="Twitter Clone app",
    description="Twitter Clone for learning FastAPI",
    version="1.0.0",
    contact={"name": "Max Mustermann", "email": "mmustermann@email.com"},
    license_info={"name": "MIT License", "url": "https://opensource.org/licenses/MIT"},
)


app.include_router(user_router)
app.include_router(post_router)
app.include_router(like_router)
app.include_router(follower_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# @app.on_event("shutdown")
# def on_shutdown():
#     drop_tables()
