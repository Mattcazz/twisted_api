from klein import Klein
from Db.db import Db
from Api.api import Api
if __name__ == "__main__":
    db =  Db()
    api = Api(db)


    

