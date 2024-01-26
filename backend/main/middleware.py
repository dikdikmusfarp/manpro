from django.middleware.common import CommonMiddleware

class CorsMiddleware(CommonMiddleware):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:3000"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        return response