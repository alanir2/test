from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.sign_up_by_django),



]