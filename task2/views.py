from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string




def index(request):
    # t=render_to_string('second_task/class_template.html')
    # return HttpResponse(t)
    return render(request, 'second_task/class_template.html')

class index2(TemplateView):
    template_name = 'func_template.http'
