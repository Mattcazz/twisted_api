import os 

class Db():
    def __init__(self):
        if not os.path.exists("./Db/data/users"):
            os.makedirs("./Db/data/users")

    def get_path(self) -> str: 
        return "Db/data"