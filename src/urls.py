from rest_framework import routers
from .api import ConnectedEmailViewSet, ConnectNewAccountViewSet, SingleEmailViewSet, EmailDetailsViewSet, ConnectedAddressesViewSet, EmailFromLabelViewSet, McwFromLabelViewSet
# from django.conf.urls import url

router = routers.DefaultRouter()
router.register('api/et', ConnectedEmailViewSet, 'et')
router.register('api/connectNewEmail',
                ConnectNewAccountViewSet, 'connectNewEmail')
router.register('api/singleEmail', SingleEmailViewSet, 'singleEmail')
router.register('api/emailDetails', EmailDetailsViewSet, 'emailDetails')
router.register('api/connectedAddresses',
                ConnectedAddressesViewSet, 'connectedAddresses')
router.register('api/emailFromLabel', EmailFromLabelViewSet, 'emailFromLabel')
router.register('api/mostCommon', McwFromLabelViewSet, 'mostCommon')

urlpatterns = router.urls
