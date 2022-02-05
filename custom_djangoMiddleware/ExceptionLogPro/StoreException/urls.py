from django.urls import path
from .views import RaiseException,ApiEndpointList
urlpatterns = [
    path("",ApiEndpointList.as_view()),
    path("GenerateException/",RaiseException.as_view())
]