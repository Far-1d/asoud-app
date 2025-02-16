from django.urls import path

from apps.market.views.owner_views import (
    MarketCreateAPIView,
    MarketUpdateAPIView,
    MarketListAPIView,
    MarketLocationCreateAPIView,
    MarketLocationUpdateAPIView,
    MarketContactCreateAPIView,
    MarketContactUpdateAPIView,
    MarketInactiveAPIView,
    MarketQueueAPIView,
    MarketLogoAPIView,
    MarketBackgroundAPIView,
    MarketSliderAPIView,
    MarketThemeAPIView,
)

app_name = 'market_owner'

urlpatterns = [
    path(
        'create/',
        MarketCreateAPIView.as_view(),
        name='create',
    ),
    path(
        'update/<int:pk>/',
        MarketUpdateAPIView.as_view(),
        name='update',
    ),
    path(
        'list/',
        MarketListAPIView.as_view(),
        name='list',
    ),
    path(
        'location/create/',
        MarketLocationCreateAPIView.as_view(),
        name='location-create',
    ),
    path(
        'location/update/<int:pk>/',
        MarketLocationUpdateAPIView.as_view(),
        name='location-update',
    ),
    path(
        'contact/create/',
        MarketContactCreateAPIView.as_view(),
        name='contact',
    ),
    path(
        'contact/update/<int:pk>/',
        MarketContactUpdateAPIView.as_view(),
        name='contact',
    ),
    path(
        'inactive/<int:pk>/',
        MarketInactiveAPIView.as_view(),
        name='inactive',
    ),
    path(
        'queue/<int:pk>/',
        MarketQueueAPIView.as_view(),
        name='queue',
    ),
    path(
        'logo/<int:pk>/',
        MarketLogoAPIView.as_view(),
        name='logo',
    ),
    path(
        'background/<int:pk>/',
        MarketBackgroundAPIView.as_view(),
        name='background',
    ),
    path(
        'slider/<int:pk>/',
        MarketSliderAPIView.as_view(),
        name='slider',
    ),
    path(
        'theme/<int:pk>/',
        MarketThemeAPIView.as_view(),
        name='theme',
    ),
]
