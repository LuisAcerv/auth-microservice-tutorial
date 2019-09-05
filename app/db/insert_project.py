from app.db.database import Database
from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from uuid import uuid4
import json

base = declarative_base()

class InsertProject(base):
    db_string='postgresql://user:password@localhost/authdb'
    db = create_engine(db_string)  
    base = declarative_base()
    __tablename__ = 'projects'


    project_id = Column(String, primary_key=True)
    project_name = Column(String)
    Session = sessionmaker(db)  
    session = Session()

    def createProject(self, name, new_client=None, new_id=None):
        try:
            new_client = InsertProject(project_id=uuid4(), project_name=name)
            InsertProject.session.add(new_client)  

            InsertProject.session.flush()
            new_id = str(new_client.project_id)
            print(new_id)

            return {'id': new_id, 'name':name}
        except:
            InsertProject.session.rollback()
            raise
        finally:
            InsertProject.session.close()