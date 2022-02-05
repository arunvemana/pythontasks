from django.urls import path
from .views import GetException
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("",csrf_exempt(GetException.as_view()))
]