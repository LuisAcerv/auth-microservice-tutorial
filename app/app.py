import falcon
from falcon_cors import CORS

from falcon_auth import FalconAuthMiddleware, TokenAuthBackend
from app.routes.create_user import CreateUser
from app.routes.create_project import CreateProject


cors = CORS(allow_origins_list=['http://localhost:8080'])

# a loader function to fetch user from username, password
user_loader = lambda username, password: { 'username': username }

# basic auth backend
token_auth = TokenAuthBackend(user_loader=lambda token: {'id':'123'})

auth_middleware = FalconAuthMiddleware(token_auth, exempt_routes=['/api/v1/create-project'])

api = falcon.API(middleware=[auth_middleware, cors.middleware])

public_cors = CORS(allow_all_origins=True)

api.add_route('/api/v1/create-user', CreateUser())
api.add_route('/api/v1/create-project', CreateProject())