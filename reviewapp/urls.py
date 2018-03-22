"""reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, \
    refresh_jwt_token, verify_jwt_token

api_urls = [
    url(r'^', include('api.urls', namespace='reviews')),
    url(r'^login', obtain_jwt_token,  name='login'),
    url(r'^token/refresh', refresh_jwt_token, name='refresh'),
    url(r'^token/verify', verify_jwt_token, name='verify'),
]

urlpatterns = [
    #url(r'^admin/', admin.site.urls), #Uncomment if you wish to use django admin
    url(r'^api/v1/', include(api_urls)),
]