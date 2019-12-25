from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserViewSet.user_create, name='user'),
    path('<int:pk>', views.UserViewSet.user, name='user_detail'),
]