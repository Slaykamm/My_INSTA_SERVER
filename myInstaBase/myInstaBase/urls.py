"""myInstaBase URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from storage import views

router = routers.DefaultRouter()
router.register(r'api/video', views.VideoViewSet)
router.register(r'api/author', views.AuthorViewSet)
router.register(r'api/comments', views.CommentsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/video/', include('storage.urls')),
    path('api/author/', include('storage.urls')),
    path('api/comments/', include('storage.urls')),
    path('', include(router.urls)),
]


# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)