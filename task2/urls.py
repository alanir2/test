from django.contrib import admin
from django.urls import path, include
from task2.views import index, index2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index2.as_view())
]
