from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'login', views.LoginViewSet, basename='Login')

urlpatterns = router.urls