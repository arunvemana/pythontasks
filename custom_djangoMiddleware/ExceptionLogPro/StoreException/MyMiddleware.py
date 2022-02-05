import sqlite3

from ExceptionLogPro import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import  HttpResponse,JsonResponse
from .models import StoreException
from ExceptionLogPro.settings import ERROR_LIST
import logging

class ErrorLogMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        if response.status_code in ERROR_LIST:
            message = response.status_code
            body = response.content
            # print(body.decode('ascii'))
            try:
                store_data = StoreException(error_code=int(message),
                                            error_type=response.title,
                                            error_traceback=body.decode('ascii'))
                store_data.save()
                response = response.title
            except sqlite3.OperationalError as e:
                logging.exception(f"DataBase was locked, disconnect any connect:-{e}")
            finally:
                return JsonResponse({'status_code':200,"error":str(response)},status=200)
        else:
            return response