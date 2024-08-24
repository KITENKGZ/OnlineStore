from re import DEBUG
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog'))
] + debug_toolbar_urls()