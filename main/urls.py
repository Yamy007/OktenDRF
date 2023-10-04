from .views import *
from django.urls import path

urlpatterns = [
    path('api', CarListCreate.as_view()),
    path('api/<int:pk>', CarViewUpdateDelete.as_view())
]
