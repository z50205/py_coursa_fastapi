from sqlmodel import Field, Session, SQLModel,select,insert,update
import datetime
from typing import Optional
from . import engine
import io,uuid

from passlib.hash import pbkdf2_sha256

class User(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    username: str= Field(unique=True)
    password_hash: str= Field()
    name: str= Field()
    email: str= Field(unique=True)
    role:bool=Field(default=False)
    create_time: str = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    def set_pw(self,password):
        return pbkdf2_sha256.hash(password)
    def check_pw(self,password):
        return pbkdf2_sha256.verify(password, self.password_hash)

    @classmethod
    def query_users_by_name(self,username:str):
        with Session(engine) as session:
            user=session.exec(select(User).where(User.name==username)).one_or_none()
            return user
    @classmethod
    def query_users_by_id(self,id:str):
        with Session(engine) as session:
            user=session.exec(select(User).where(User.id==id)).one_or_none()
            return user
        
    @classmethod
    def query_teachers(self):
        with Session(engine) as session:
            teachers=session.exec(select(User).where(User.role==True)).fetchall()
            return teachers
        
    @classmethod
    def create_users(self,username:str,password:str,name:str,email:str,is_insturctor:bool):
        with Session(engine) as session:
            dt = datetime.datetime.now(datetime.timezone.utc)
            dt_sec = dt.isoformat(timespec='seconds') 
            dt_iso = dt_sec.replace("+00:00", "Z")
            u=User(id=uuid.uuid4(),username=username,password_hash=self.set_pw(self,password),name=name,email=email,create_time=dt_iso,role=is_insturctor)
            session.add(u)
            session.commit()