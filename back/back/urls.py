"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp import views
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'games', views.Games1ViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title='Soft Loading API',
      default_version='v1',
      description='Is used to see and download soft',
      # contact=openapi.Contact(email='contact@snippets.local'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kupigru/', views.hello),
    path('list/', views.gameList),
    path('game/<int:id>/', views.GetGame, name='game_url'),
    path('', include(router.urls)),path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='API-swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='API-redoc'),
    path('api.yaml', schema_view.without_ui(cache_timeout=0), name='API-yaml'),
    path('api.json', schema_view.without_ui(cache_timeout=0), name='API-json')
]