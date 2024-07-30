from django.urls import path, include
from . import views
urlpatterns = [
    path('platform/', views.platform),
    path('platform/cart/', views.index),
    path('platform/games/', views.categories)


]