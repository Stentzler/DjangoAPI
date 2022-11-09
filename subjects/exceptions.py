from rest_framework.exceptions import APIException
from rest_framework.views import status


class NonUpdatableKeyError(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY