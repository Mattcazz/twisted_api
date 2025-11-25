from klein import Klein
from Handlers.UserHandler import UserHandler
from repositories.UserRepo import UserRepo

class Api():
    def __init__(self, db):
        self.app = Klein()
        self.db = db 
        self.register_routes()
        userRepo = UserRepo(db)
        self.userHandler = UserHandler(userRepo)

    def run(self, host : str, port : str):
        self.app.run(host, port)
    
    def register_routes(self):
        self.app.route("users/<id>")(self.userHandler.get_user_by_id)

    
