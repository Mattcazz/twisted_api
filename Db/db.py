import os 

class Db():
    def __init__(self):
        if not os.path.exists("./data/users"):
            os.makedirs("./data/users")

    def get_path(self) -> str: 
        return "/db/data"