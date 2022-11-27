"""mood_metr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


from blog.views import day_detail_view, all_estimate_view, estimate_create_view, delete_estimate
from core.views import home_page

from accounts.views import *

urlpatterns = [
	path('login/', loginPage, name='login'),
	path('register/', registerPage, name='register'),
	path('blog/', day_detail_view),
	path('home_page/', home_page, name='home'),
	path('all_days/', all_estimate_view, name='all_days'),
	path('create_estimate/', estimate_create_view, name='create_estimate'),
	path('logout_user/', logout_user, name='logout' ),
    path('admin/', admin.site.urls),
	path('delete_estimate/<estimate_id>', delete_estimate, name='delete'),
]
