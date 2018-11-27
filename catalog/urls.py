from django.urls import path ,re_path
from .views import ProductList, ProductDetail
"""Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

urlpatterns = [
    re_path(r'^$',ProductList, name='ProductList'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', ProductList, name='ProductListByCategory'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetail, name='ProductDetail'),
]