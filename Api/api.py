from klein import Klein
from Api.Handlers.UserHandler import UserHandler
from repositories.UserRepo import UserRepo

class Api():
    def __init__(self, db):

        self.app = Klein()
        self.db = db 

        userRepo = UserRepo(db)
        self.userHandler = UserHandler(userRepo)
        self.register_routes()


    def run(self, host : str, port : str):
        self.app.run(host, port)
    
    def register_routes(self):
        self.app.route("/users/<id>", methods=["GET"])(self.userHandler.get_user_by_id)
        self.app.route("/users", methods=["POST"])(self.userHandler.create_user)

    
