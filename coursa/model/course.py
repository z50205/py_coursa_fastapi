from sqlmodel import Field, Session, SQLModel,select,insert,update
import datetime
from typing import Optional
from . import engine
import io,uuid

class Course(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str=Field(unique=True)
    description: str=Field()
    weekday: str=Field()
    start: str=Field()
    end: str=Field()
    location: str=Field()
    create_time: str = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))
    # 每一個課程區間(時間、授課教室)對課程也應以mxm設計(類似授課教師、學生對課程)；為開發基本功能先假設課程區間對課程1x1
    
    @classmethod
    def query_courses_by_name(self,course_name:str):
        with Session(engine) as session:
            course=session.exec(select(Course).where(Course.name==course_name)).one_or_none()
            return course
        
    @classmethod
    def update_courses(self,courseid:str,coursename:str,description:str,weekday:str,start:str,end:str,location:str):
        with Session(engine) as session:
            course=session.exec(select(Course).where(Course.id==courseid)).one_or_none()
            course.name=coursename
            course.description=description
            course.weekday=weekday
            course.start=start
            course.end=end
            course.location=location
            session.add(course)
            session.commit()
            session.refresh(course)
        
    @classmethod
    def create_courses(self,coursename:str,description:str,weekday:str,start:str,end:str,location:str):
        with Session(engine) as session:
            dt = datetime.datetime.now(datetime.timezone.utc)
            dt_sec = dt.isoformat(timespec='seconds') 
            dt_iso = dt_sec.replace("+00:00", "Z")
            c=Course(id=uuid.uuid4(),name=coursename,description=description,weekday=weekday,start=start,end=end,location=location,create_time=dt_iso)
            session.add(c)
            session.commit()
            return c.id
        
    @classmethod
    def delete_courses(self,courseid:str):
        with Session(engine) as session:
            course=session.exec(select(Course).where(Course.id==courseid)).one_or_none()
            session.delete(course)
            session.commit()

    