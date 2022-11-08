from rest_framework.exceptions import APIException
from rest_framework.views import status


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    
class Unauthorized(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED    