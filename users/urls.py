from rest_framework import routers
from .api import ConnectedEmailViewSet

router = routers.DefaultRouter()
router.register('api/et', ConnectedEmailViewSet, 'et')

urlpatterns = router.urls
