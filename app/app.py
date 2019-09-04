import falcon
from app.routes.create_user import CreateUser

api = falcon.API()

api.add_route('/api/v1/create-user', CreateUser())