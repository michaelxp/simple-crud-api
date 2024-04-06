
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from games.api import viewsets

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

route = routers.DefaultRouter()

route.register(r'api', viewsets.GamesViewSet, basename='Games')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('',include(route.urls))
]
