from django.contrib import admin
from django.urls import path
from app.views import test_cache
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_cache, name='test_cache'),
]
