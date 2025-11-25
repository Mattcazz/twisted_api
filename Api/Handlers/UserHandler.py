from repositories.UserRepo import UserRepo
from Api.Schemas.UserSchema import UserSchema
import json
from twisted.web.server import Request
from Api.Handlers.BaseHandler import  BaseHandler


class UserHandler(BaseHandler):
    def __init__(self, repo : UserRepo):
        self.repo = repo
        self.userSchema = UserSchema()
    
    def get_user_by_id(self, request : Request, id : int):
        request.setHeader('Content-Type', 'application/json')

        user = self.repo.get_user_by_id(id)
        
        if user is None: 
            return self.write_error(request, "user not found", 404)

        user_data = self.userSchema.dump(user) 

        request.setResponseCode(200)
        return json.dumps(user_data).encode("utf-8")
    
    def create_user(self, request : Request):
        request.setHeader('Content-Type', 'application/json')
        
        try: 
            user = self.parse_json_request(request, self.userSchema)
        except ValueError as e:
            return self.write_error(request, str(e), 400)
        
        (err, err_str, user) = self.repo.create_user(user)

        if err:
            return self.write_error(request, err_str, 404)
        
        user_data = self.userSchema.dump(user) 
        
        return self.write_json_response(request, user_data, 201)


