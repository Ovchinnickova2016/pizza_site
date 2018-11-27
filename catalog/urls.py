from django.urls import path ,re_path
from .views import index, login, register, contacts, delivery, vacations
"""Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

urlpatterns = [
    re_path(r'^$',index, name='index'),
    re_path(r'^login', login, name='login'),
    re_path(r'^register', register, name='register'),
    re_path(r'^contacts', contacts, name='contacts'),
    re_path(r'^delivery', delivery, name='delivery'),
    re_path(r'^vacations', vacations, name='vacations'),
]