from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('cart/', views.platform),
    path('games/', views.categories)


]