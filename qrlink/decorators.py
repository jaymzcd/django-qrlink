from qrlink.middleware import QrlinkMiddleware
from django.utils.decorators import decorator_from_middleware

qrlink = decorator_from_middleware(QrlinkMiddleware)