from rest_framework import routers
from .api import CatAlgViewSet

router = routers.DefaultRouter()
router.register('api/catAlg', CatAlgViewSet, 'catAlg')

urlpatterns = router.urls
