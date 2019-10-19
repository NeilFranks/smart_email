from rest_framework import routers
from .api import CatAlgViewSet, TestObjectViewSet

router = routers.DefaultRouter()
router.register('api/catAlg', CatAlgViewSet, 'catAlg')
router.register('api/testObject', TestObjectViewSet, 'testObject')


urlpatterns = router.urls
