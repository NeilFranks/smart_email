from rest_framework import routers
from .api import EmailTokenViewSet

router = routers.DefaultRouter()
router.register('api/et', EmailTokenViewSet, 'et')

urlpatterns = router.urls
