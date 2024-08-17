from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView




def index(request):
    # t=render_to_string('second_task/class_template.html')
    # return HttpResponse(t)
    return render(request, 'second_task/func_template.html')

# def categories(request):
#     # return HttpResponse('Страница приложения cat')
#     return render(request, 'second_task/func_template.html')

class index2(TemplateView):
    template_name = 'second_task/class_template.html'