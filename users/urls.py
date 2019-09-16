from rest_framework import routers
from .api import CatAlgViewSet, EmailLoginViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('api/catAlg', CatAlgViewSet, 'catAlg')
router.register('api/emailLogin', EmailLoginViewSet, 'emailLogin')
router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls
