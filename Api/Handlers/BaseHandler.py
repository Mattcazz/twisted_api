import json 
from marshmallow import Schema

class BaseHandler():

    def parse_json_request(self, request, schema : Schema):
        try:
            length = int(request.getHeader("Content-Length"))
            body_bytes = request.content.read(length)
            data = json.loads(body_bytes.decode("utf-8"))
        except Exception as e:
            raise ValueError("Invalid JSON body") from e

        return schema.load(data)

    def write_json_response(self, request, data, status_code=200):
        request.setResponseCode(status_code)
        request.setHeader(b"Content-Type", b"application/json")
        return json.dumps(data).encode("utf-8")

    def write_error(self, request, message, status_code=400):
        return self.write_json_response(request, {"error": message}, status_code)