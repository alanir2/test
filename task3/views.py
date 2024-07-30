from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    # t=render_to_string('task3/templates/third_task/cart.html')
    # return HttpResponse('jfh')
    return render(request, 'third_task/cart.html')

def categories(request):
    # return HttpResponse('Страница приложения cat')
    return render(request, 'third_task/games.html')

def platform(request):
    return render(request,'third_task/platform.html')
