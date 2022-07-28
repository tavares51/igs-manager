"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework import routers
from igsManager.views import EmployeeViewSet, DepartamentViewSet
from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet, basename='Employee')
router.register('departament', DepartamentViewSet, basename='Departament')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 
        include([
                path('', include(router.urls)), 
                path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")
            ])
        ),
    path('list-employees/', include('igsManager.urls')),
]
