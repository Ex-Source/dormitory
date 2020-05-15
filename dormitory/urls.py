"""dormitory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import xadmin

from django.contrib import admin
from django.urls import path
from xadmin.plugins import xversion

from management.views import SelectView
from student import views

xadmin.autodiscover()
xversion.register_models()
urlpatterns = [
    path('index/pw/',views.pw),
    path('index/',views.index),
    path('index/info/',views.info),
    path('index/pay/',views.pay),
    path('index/repair/',views.repair),
    path('student/',views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('xadmin/', xadmin.site.urls),
    path('select/building_room/?module=', SelectView.as_view(), name='building_room'),
    path('admin/', admin.site.urls),
]
