from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index2),
    path('index/', TemplateView.as_view(template_name = 'index2'))
]