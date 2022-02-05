from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from ExceptionLogPro.settings import ERROR_LIST
import random
from requests import exceptions

import traceback


# Create your views here.
class RaiseException(View):
    def get(self, request):
        try:
            data = random.choice(dir(exceptions))
            raise Exception(data)
        except Exception as e:
            response = HttpResponse()
            response.status_code = random.choice(ERROR_LIST)
            response.title = e
            response.content = traceback.format_exception(e)
            return response


class ApiEndpointList(View):
    def get(self,request):
        return JsonResponse({"Get":{"First":
                                        {"url":"GenerateException/",
                                         "Method":"GET",
                                         "Use":"To Generate new Exception to store in Database"},
                                    "Second":
                                        {"url":"FilterException/",
                                         "Method":"GET",
                                         "Params": "id",
                                         "Use":"To see all the Excception stored in database,also filter to see"
                                               "Entery based on id"}},
                             "Post":{"First":
                                         {"url":"FilterException/",
                                          "Method":"POST",
                                          "body":"form-data with id has key",
                                          "Use":"To deleted the Exception from data based on ID"}}},status=200)

