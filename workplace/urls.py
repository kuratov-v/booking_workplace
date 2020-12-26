from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workplace import views

router = DefaultRouter()

router.register('workplace', views.WorkplaceView, basename='Workplace')
router.register('booking', views.BookingView, basename='Booking')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
