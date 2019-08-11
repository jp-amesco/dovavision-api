from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='User')

urlpatterns = router.urls