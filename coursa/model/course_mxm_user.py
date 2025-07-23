from sqlmodel import Field, Session, SQLModel,select,insert,update
import datetime
from typing import Optional
from . import engine,Course,User
import io,uuid

class CourseUser(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    course_id: str= Field(nullable=False, foreign_key="course.id",ondelete="CASCADE")
    user_id: str= Field(nullable=False, foreign_key="user.id",ondelete="CASCADE")
    role: int =Field(default=0)
    # 考量course對user屬mxm，又可能有多個授課教師、多個學生、教師或許也可以當某堂課的學生，將【角色欄位(role)】放到此中介表內，而非user裡面

    @classmethod
    def query_courses(self):
        with Session(engine) as session:
            course_infos=session.exec(select(Course, User).select_from(CourseUser).join(Course, Course.id == CourseUser.course_id).join(User, User.id == CourseUser.user_id).where(CourseUser.role == True)).fetchall()
            return course_infos
    
    @classmethod
    def query_courses_by_teachername(self,teachername:str):
        with Session(engine) as session:
            course_infos=session.exec(select(Course, User).select_from(CourseUser).join(Course, Course.id == CourseUser.course_id).join(User, User.id == CourseUser.user_id).where(CourseUser.role == True).where(User.name ==teachername)).fetchall()
            return course_infos
    @classmethod
    def query_courses_by_courseid(self,course_id:str):
        with Session(engine) as session:
            course_infos=session.exec(select(Course, User).select_from(CourseUser).join(Course, Course.id == CourseUser.course_id).join(User, User.id == CourseUser.user_id).where(CourseUser.role == True).where(Course.id ==course_id)).fetchall()
            return course_infos
        
    @classmethod
    def update_courses_teacher(self,courseid:str,instructor_origin:str,instructor:str):
        with Session(engine) as session:
            cu=session.exec(select(CourseUser).where(CourseUser.course_id ==courseid).where(CourseUser.user_id ==instructor_origin)).one_or_none()
            cu.user_id=instructor
            session.add(cu)
            session.commit()
            session.refresh(cu)

    @classmethod
    def create_courses_teacher(self,course_id,teacher_id:str):
        with Session(engine) as session:
            cu=CourseUser(id=uuid.uuid4(),course_id=course_id,user_id=teacher_id,role=True)
            session.add(cu)
            session.commit()