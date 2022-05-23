"""config URL Configuration

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

from django.urls import path

import cart.views
import users.views

from cart import views
#
app_name = 'users'
urlpatterns = [
    path('', cart.views.detail, name='mypage'),
    path('coupon/', users.views.coupon, name='coupon'),
    path('update/', users.views.update, name='update'),
    path('deletepage/', users.views.deletepage, name='deletepage'),
    path('delete/', users.views.delete, name='delete'),

]
#
