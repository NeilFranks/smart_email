from rest_framework import routers
from .api import ConnectedEmailViewSet, ConnectNewAccountViewSet, SingleEmailViewSet, EmailDetailsViewSet, ConnectedAddressesViewSet
# from django.conf.urls import url

router = routers.DefaultRouter()
router.register('api/et', ConnectedEmailViewSet, 'et')
router.register('api/connectNewEmail',
                ConnectNewAccountViewSet, 'connectNewEmail')
router.register('api/singleEmail', SingleEmailViewSet, 'singleEmail')
router.register('api/emailDetails', EmailDetailsViewSet, 'emailDetails')
router.register('api/connectedAddresses',
                ConnectedAddressesViewSet, 'connectedAddresses')

urlpatterns = router.urls
