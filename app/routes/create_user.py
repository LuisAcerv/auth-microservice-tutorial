import falcon
import json

class CreateUser(object):
    def on_post(self, req, resp):
        """
            Handle create user request
        """
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({
            'hello':'world'
        })