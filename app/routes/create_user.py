import falcon
import json
import re
from voluptuous import MultipleInvalid, Schema, All,validate, Invalid

class CreateUser(object):
    def Email(msg=None):
        """
            Validate email
        """
        def f(v):
            if re.match("[\w\.\-]*@[\w\.\-]*\.\w+", str(v)):
                return str(v)
            else:
                raise Invalid(msg or ("incorrect email address"))
        return f

    def Password(msg=None):
        def validate(password):
            while True:
                if len(password) < 8:
                    raise Invalid(msg or "Make sure your password is at lest 8 letters")
                elif re.search('[0-9]',password) is None:
                    raise Invalid(msg or "Make sure your password has a number in it")
                elif re.search('[A-Z]',password) is None: 
                    raise Invalid(msg or "Make sure your password has a capital letter in it")
                else:
                    break
            
        return validate

    validation = Schema({'email': All(Email()), 'password': All(Password())}, required=True)

    def on_post(self, req, resp):
        """
            Handle create user request
        """
        # Handle request data
        try:
            data = json.load(req.stream)
            validate(CreateUser.validation(data))
        except MultipleInvalid as e:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'error':'%s %s' % (e.msg, e.path)})
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                'hello':'world'
            })