from django.contrib import admin
from django.urls import path

from core.views import (
    index,
    contact,
    product,
    product_list,
)

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contact'),
    path('produto/', product, name='product'),
    path('produtos/', product_list, name='product_list'),
    path('admin/', admin.site.urls),
]
