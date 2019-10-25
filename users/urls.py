from rest_framework import routers
from .api import EmailPassViewSet

router = routers.DefaultRouter()
router.register('api/ep', EmailPassViewSet, 'ep')

urlpatterns = router.urls
