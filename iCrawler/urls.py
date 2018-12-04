from django.contrib import admin
from django.urls import path
#API
from django.conf import settings
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter  
from django.conf.urls import url, include

urlpatterns = [
    #url(r'api/v1/', include(('main.urls', 'main'), namespace='main')),
    path('api/v1/', include('main.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
]