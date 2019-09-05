from app.db.insert_project import InsertProject
import falcon
import json
import re
from voluptuous import MultipleInvalid, Schema, All,validate, Invalid
from sqlalchemy.dialects import postgresql

class CreateProject(object):

    validation = Schema({'project_name': str}, required=True)

    def on_post(self, req, resp, new_client=None):
        '''
            Handle create project request
        '''
        # Handle request data
        try:
            data = json.load(req.stream)

            validate(CreateProject.validation(data))
            new_client = InsertProject().createProject(data['project_name'])
        except MultipleInvalid as e:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'error':'%s %s' % (e.msg, e.path)})
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({ 'data': new_client , 'success':True, 'code': 200})