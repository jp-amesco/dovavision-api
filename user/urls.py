from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user'),
    path('create', views.UserCreate.as_view(), name='user.create'),
]