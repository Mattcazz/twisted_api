import os
from Models.User import User
import json
from typing import Optional
from Db.db import Db

class UserRepo():

    _next_id = 1

    def __init__(self, db : Db):
        self.db_path = os.path.join(db.get_path(), f"users")
        
    
    def get_user_by_id(self, id : int) -> Optional[User]:
        file_path = os.path.join(self.db_path, f"{id}.txt")

        if not os.path.exists(file_path):
            return None 
        
        with open(file_path, "r") as f:
            data = json.load(f)
            user = User(**data)
        
        return user
    
    def create_user(self, user : User) -> tuple[bool, str, Optional[User]]:

        UserRepo._next_id += 1
        user.id = UserRepo._next_id
        
        file_path =  os.path.join(self.db_path, f"{user.id}.txt")

        if os.path.exists(file_path):
            UserRepo._next_id -= 1
            return (True, f"error: user already exists", None) 
        
        user_data = user.__dict__

        with open(file_path, "w") as f: 
            json.dump(user_data, f, indent=4)
        
       
        return False, "", user