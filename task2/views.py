from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView




def index(request):

    return render(request, 'second_task/func_template.html')

class index2(TemplateView):
    template_name = 'class_template.html'
