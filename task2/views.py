from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string




def index(request):
    # t=render_to_string('second_task/class_template.html')
    # return HttpResponse(t)
    return render(request, 'second_task/class_template.html')

def categories(request):
    # return HttpResponse('Страница приложения cat')
    return render(request, 'second_task/func_template.html')
