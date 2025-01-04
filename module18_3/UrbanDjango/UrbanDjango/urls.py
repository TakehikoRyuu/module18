"""
URL configuration for UrbanDjango project.

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
from task2.views import func_temp, class_temp
from task3.views import cart_temp, games_temp, platform_temp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', class_temp, name='class_view'),  # Связываем ClassView с URL /class/
    path('func/', func_temp, name='func_view'),  # Связываем func_view с URL /func/

    path('platform/cart/', cart_temp, name='cart_view'),  # Связываем func_view с URL /func/
    path('platform/games/', games_temp, name='games_view'),  # Связываем func_view с URL /func/
    path('platform/', platform_temp, name='platform_view'),  # Связываем func_view с URL /func/
]