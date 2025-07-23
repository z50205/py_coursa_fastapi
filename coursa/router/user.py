from fastapi import APIRouter,Request,Form
from typing import Union

from model import User,CourseUser
from fastapi.responses import JSONResponse
from .api_user_docs import post_api_users,get_api_teachers,get_api_teachers_courses,get_api_teachers_courses_by_teachername

user_router = APIRouter()

@user_router.get("/api/teachers",**get_api_teachers)
async def read_teachers(request:Request):
    result={}
    teachers=User.query_teachers()
    for teacher in teachers:
        teacher_id = str(teacher.id)
        if teacher_id not in result:
            result[teacher_id]={"teacher_name":teacher.name}
    return JSONResponse(status_code=200,content=result)

@user_router.get("/api/teachers/courses",**get_api_teachers_courses)
async def read_teachers(request:Request):
    result={}
    course_infos=CourseUser.query_courses()
    for course_info in course_infos:
        course = course_info[0]
        teacher = course_info[1]
        teacher_id = str(teacher.id)
        if teacher_id not in result:
            result[teacher_id]={"teacher_name":teacher.name,"teacher_email":teacher.email,"courses":[]}
        result[teacher_id]["courses"].append({"name":course.name})
    return JSONResponse(status_code=200,content=result)

@user_router.get("/api/teachers/{teachername}/courses",**get_api_teachers_courses_by_teachername)
async def read_course_by_teacher(request:Request,teachername:str):
    result={}
    course_infos=CourseUser.query_courses_by_teachername(teachername)
    for course_info in course_infos:
        course = course_info[0]
        course_id = str(course.id)
        if course_id not in result:
            result[course_id]={"course_name":course.name,"weekday":course.weekday,"start":course.start,"end":course.end,"description":course.description,"location":course.location}
    return JSONResponse(status_code=200,content=result)

@user_router.post("/api/users",**post_api_users)
async def create_user(request:Request,username:str=Form(...),password:str=Form(...),name:str=Form(...),email:str=Form(...),is_instructor: bool = Form(False)):
    # instructor 應該有驗證碼為宜
    u=User.query_users_by_name(username)
    if u==None:
        User.create_users(username,password,name,email,is_instructor)
        return JSONResponse(status_code=201,content={"status":"ok","detail":"create user success."})
    else:
        return JSONResponse(status_code=409,content={"status":"fail","detail":"duplicate user name."})