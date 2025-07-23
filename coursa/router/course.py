from fastapi import APIRouter,Request,Form
from typing import Union

from model import User,Course,CourseUser
from fastapi.responses import JSONResponse
from .api_course_docs import get_api_courses,post_api_courses,patch_api_courses,delete_api_courses,get_api_courses_by_courseid

course_router = APIRouter()

@course_router.get("/api/courses",**get_api_courses)
async def read_course(request:Request):
    result={}
    course_infos=CourseUser.query_courses()
    for course_info in course_infos:
        course = course_info[0]
        teacher = course_info[1]
        course_id = str(course.id)
        if course_id not in result:
            result[course_id]={"course_name":course.name,"weekday":course.weekday,"start":course.start,"end":course.end,"description":course.description,"location":course.location,"teachers":[]}
        result[course_info[0].id]["teachers"].append({"name":teacher.name,"email":teacher.email})
    return JSONResponse(status_code=200,content=result)

@course_router.post("/api/courses",**post_api_courses)
async def create_course(request:Request,coursename:str=Form(...),description:str=Form(...),weekday:str=Form(...),start:str=Form(...),end:str=Form(...),instructor:str=Form(...),location:str=Form(...)):
    course=Course.query_courses_by_name(coursename)
    user=User.query_users_by_id(instructor)
    if course==None:
        if user.role:
            course_id=Course.create_courses(coursename,description,weekday,start,end,location)
            CourseUser.create_courses_teacher(course_id,instructor)
            return JSONResponse(status_code=201,content={"status":"ok","detail":"create course success."})
        else:
            return JSONResponse(status_code=403,content={"status":"fail","detail":"authorization failed."})
    else:
        return JSONResponse(status_code=409,content={"status":"fail","detail":"duplicate course name."})

@course_router.patch("/api/courses/{course_id}",**patch_api_courses)
async def update_course(request:Request,course_id:str,coursename:str=Form(...),description:str=Form(...),weekday:str=Form(...),start:str=Form(...),end:str=Form(...),instructor:str=Form(...),instructor_origin:str=Form(...),location:str=Form(...)):
    course=Course.query_courses_by_name(coursename)
    user=User.query_users_by_id(instructor)
    if course==None or course.id==course_id:
        if user.role:
            Course.update_courses(course_id,coursename,description,weekday,start,end,location)
            CourseUser.update_courses_teacher(course_id,instructor_origin,instructor)
            return JSONResponse(status_code=200,content={"status":"ok","detail":"update course success."})
        else:
            return JSONResponse(status_code=403,content={"status":"fail","detail":"authorization failed."})
    else:
        return JSONResponse(status_code=409,content={"status":"fail","detail":"duplicate course name."})

@course_router.delete("/api/courses/{course_id}",**delete_api_courses)
async def delete_course(request:Request,course_id:str):
    Course.delete_courses(course_id)
    return JSONResponse(status_code=200,content={"status":"ok","detail":"delete course success."})

@course_router.get("/api/courses/{course_id}",**get_api_courses_by_courseid)
async def read_course(request:Request,course_id:str):
    result={}
    course_infos=CourseUser.query_courses_by_courseid(course_id)
    for course_info in course_infos:
        course = course_info[0]
        teacher = course_info[1]
        course_id = str(course.id)
        if course_id not in result:
            result[course_id]={"course_name":course.name,"weekday":course.weekday,"start":course.start,"end":course.end,"description":course.description,"location":course.location,"teachers":[]}
        result[course_info[0].id]["teachers"].append({"name":teacher.name,"id":teacher.id})
    return JSONResponse(status_code=200,content=result)