import json
import logging

from django.shortcuts import render
from django.views import View
from StoreException.models import StoreException
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

# Create your views here.


class GetException(View):
    def get(self, request):
        get_id = request.GET.get('id')
        if get_id:
            try:
                data = StoreException.objects.get(pk=int(get_id))
                data = serializers.serialize("json",[data,])
                return JsonResponse(json.loads(data)[0],safe=False)
            except ObjectDoesNotExist as e:
                return JsonResponse({"error":f"Given {get_id} is not exist in the database."})
        else:
            data = StoreException.objects.all()
            data = serializers.serialize("json",data)
            data = json.loads(data)
            return JsonResponse({"data":data,"meta":{"length":len(data)}}, safe=False)

    def post(self, request):
        get_id = request.POST.get('id')
        if get_id:
            try:
                StoreException.objects.get(pk=int(get_id)).delete()
            except Exception as e:
                logging.exception(e)
                return JsonResponse({"error": "Give `id` is not available "})
            return JsonResponse({"Success": f"given {get_id} is successful deleted from database"})
        else:
            return JsonResponse({"error": "Please provide `id` key in form-data"})
