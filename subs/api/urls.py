from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()
router.register('regions', RegionViewSet, basename='region')
router.register('provinces', ProvinceViewSet, basename='province')
router.register('municipalities', MunicipalityViewSet, basename='municipality')
router.register('barangays', BarangayViewSet, basename='barangay')
router.register('plans', PlanViewSet, basename='plan')
router.register('modems', ModemViewSets, basename='modem')
router.register('subscriptions', SubscriptionViewSet, basename='subscription')
router.register('billings', BillingViewSet, basename='billing')
router.register('payments', PaymentViewSet, basename='payment')
router.register('issues', IssueViewSet, basename='issue')
router.register('tickets', TicketViewSet, basename='ticket')
router.register('users', UserViewSet, basename='users')
router.register('subscribers', SubscriberViewSet, basename='subscribers')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),  # Djoser endpoints
    path('auth/', include('djoser.urls.jwt')),  # JWT endpoints
    path('users/me/', CurrentUserView.as_view(), name='current_user'),
    path('subscribers/choices/', SubscriberChoicesView.as_view(), name='subscriber-choices'),
]


