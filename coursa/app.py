from typing import Union

from fastapi import FastAPI

from router import course_router,user_router,view_router

app = FastAPI()
app.include_router(course_router)
app.include_router(user_router)
app.include_router(view_router)
