from django.urls import path, include
from .views.userView import UserViewSet
from .views.companyView import CompanyViewSet

urlpatterns = [
    path('user', UserViewSet.user_create, name='user'),
    path('user/<int:pk>', UserViewSet.show_or_update, name='user_detail'),
    path('user/favourite-company', UserViewSet.favourite_company, name='favourite_company'),
    path('company/<int:pk>', CompanyViewSet.show, name='company_details'),
]