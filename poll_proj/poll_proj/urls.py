"""poll_proj URL Configuration

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
# from django.conf.urls import re_path
from django.contrib import admin
from django.urls import include, path, re_path

from main.views import GenerateRandomUserView, UsersListView

urlpatterns = [
  path('', include('pages.urls')),
  path('poll_app/', include('poll_app.urls')),
  path('', include('main.urls')),
  path('admin/', admin.site.urls),
  re_path('users/', UsersListView.as_view(), name='users_list'),
  re_path('generate/', GenerateRandomUserView.as_view(), name='generate')

]
