from rest_framework import routers
from .api import (
    CategoryViewSet,
    ConnectedEmailViewSet,
    ConnectNewAccountViewSet,
    SingleEmailViewSet,
    EmailDetailsViewSet,
    ConnectedAddressesViewSet,
    EmailFromLabelViewSet,
    McwFromLabelViewSet,
    SingleMarkAsReadViewSet,
    SingleMarkAsUnreadViewSet,
    BatchMarkAsReadViewSet,
    BatchMarkAsUnreadViewSet,
    TrashViewSet,
    BatchMarkAsSomethingViewSet,
    BatchUnmarkFromSomethingViewSet,
    CreateLabelViewSet,
    RetrainLabelViewSet,
    SetPageLabelsViewSet,
)

# from django.conf.urls import url

router = routers.DefaultRouter()
router.register("api/category", CategoryViewSet, "category")
router.register("api/connectNewEmail", ConnectNewAccountViewSet, "connectNewEmail")
router.register(
    "api/connectedAddresses", ConnectedAddressesViewSet, "connectedAddresses"
)
router.register("api/emailDetails", EmailDetailsViewSet, "emailDetails")
router.register("api/emailFromLabel", EmailFromLabelViewSet, "emailFromLabel")
router.register("api/et", ConnectedEmailViewSet, "et")
router.register("api/mostCommon", McwFromLabelViewSet, "mostCommon")
router.register("api/singleEmail", SingleEmailViewSet, "singleEmail")
router.register("api/connectNewEmail", ConnectNewAccountViewSet, "connectNewEmail")
router.register(
    "api/connectedAddresses", ConnectedAddressesViewSet, "connectedAddresses"
)
router.register("api/singleMarkAsRead", SingleMarkAsReadViewSet, "singleMarkAsRead")
router.register(
    "api/singleMarkAsUnread", SingleMarkAsUnreadViewSet, "singleMarkAsUnread"
)
router.register("api/batchMarkAsRead", BatchMarkAsReadViewSet, "batchMarkAsRead")
router.register("api/batchMarkAsUnread", BatchMarkAsUnreadViewSet, "batchMarkAsUnread")
router.register("api/trashMessage", TrashViewSet, "trashMessage")
router.register(
    "api/batcDhMarkAsSomething", BatchMarkAsSomethingViewSet, "batchMarkAsSomething"
)
router.register(
    "api/batchUnmarkFromSomething",
    BatchUnmarkFromSomethingViewSet,
    "batchUnmarkFromSomething",
)
router.register("api/setPageLabel", SetPageLabelsViewSet, "setPageLabel")
router.register("api/createLabel", CreateLabelViewSet, "createLabel")
router.register("api/retrainLabel", RetrainLabelViewSet, "retrainLabel")

urlpatterns = router.urls
