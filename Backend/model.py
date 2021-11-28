import json

from marshmallow import Schema, fields


class RegisterReq(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)
    firstName = fields.String(required=True)
    lastName = fields.String(required=True)
    isProfessor = fields.Boolean(required=True)


class LoginPersonReq(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class AddCourseReq(Schema):
    name = fields.String(required=True)
    code = fields.String(required=True)
    email = fields.String(required=True)


class RegisterCourseReq(Schema):
    email = fields.String(required=True)
    courseId = fields.String(required=True)


class GeneralRes:
    status_code: int
    message: str

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message
