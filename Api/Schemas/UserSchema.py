from marshmallow import Schema, fields, post_load
from Models.User import User

class UserSchema(Schema):

    id = fields.Int(required=False)
    name = fields.Str()
    email = fields.Email()
    password  = fields.Str()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)