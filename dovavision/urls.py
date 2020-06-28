from django.urls import path, include
from .views.userView import UserViewSet
from .views.companyView import CompanyViewSet

urlpatterns = [
    path('user', UserViewSet.user_create, name='user'),
    path('user/<int:pk>', UserViewSet.show_or_update, name='user_detail'),
    path('user/add-favourite-stock', UserViewSet.add_favourite_stock, name='favourite_stock'),
    path('user/remove-favourite-stock', UserViewSet.remove_favourite_stock, name='favourite_stock'),
    path('company/<int:pk>', CompanyViewSet.show, name='company_details'),
    path('company', CompanyViewSet.all, name='companies'),
    path('user/current', UserViewSet.current_user, name='currente_urser')
]