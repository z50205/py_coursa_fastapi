from fastapi import APIRouter,Request
from typing import Union

import os
from starlette.templating import Jinja2Templates

from fastapi.responses import HTMLResponse

templates_path=os.path.join("..",os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],"template")
template=Jinja2Templates(directory=templates_path)

view_router = APIRouter()

@view_router.get(
    "/",
    summary="回傳首頁頁面",
    description="載入首頁 HTML 模板，提供課程選擇系統的入口畫面。",
    response_class=HTMLResponse,
    responses={
        200: {"description": "成功載入首頁",
              "content": {
                "text/html": {
                    "example": "首頁提供查詢課程相關頁面介面及前端查詢API"
                    }
                }
            },
        404: {"description": "找不到 HTML 模板或資料"},
    },
    tags=["View"]
)
def index(request:Request):
    return template.TemplateResponse(request=request,name="index.html")

@view_router.get(
    "/courses",
    summary="回傳課程管理頁面",
    description="載入課程管理 HTML 模板，提供新建、修改及刪除課程功能畫面。",
    response_class=HTMLResponse,
    responses={
        200: {"description": "成功載入課程管理",
              "content": {
                "text/html": {
                    "example": "提供新建、修改及刪除課程功能介面及其前端API"
                    }
                }
            },
        404: {"description": "找不到 HTML 模板或資料"},
    },
    tags=["View"]
)
def course(request:Request):
    return template.TemplateResponse(request=request,name="course.html")

@view_router.get(
    "/register",
    summary="回傳用戶註冊頁面",
    description="用戶註冊 HTML 模板，提供新建用戶功能畫面。",
    response_class=HTMLResponse,
    responses={
        200: {"description": "成功載入註冊頁面",
              "content": {
                "text/html": {
                    "example": "提供新建用戶的介面及其前端API"
                    }
                }
            },
        404: {"description": "找不到 HTML 模板或資料"},
    },
    tags=["View"]
)
def register(request:Request):
    return template.TemplateResponse(request=request,name="register.html")