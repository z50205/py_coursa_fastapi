from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_DATABASE=os.environ.get("DB_DATABASE")
DB_USERNAME=os.environ.get("DB_USERNAME")
DB_PASSWORD=os.environ.get("DB_PASSWORD")

url_object="mysql+pymysql://%s:%s@%s:%s/%s" %(DB_USERNAME,DB_PASSWORD,DB_HOST,int(DB_PORT),DB_DATABASE)
engine = create_engine(url_object)

from .user import User
from .course import Course
from .course_mxm_user import CourseUser
# SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)