from django.shortcuts import render
from django.views import View

# Create your views here.


def func_temp(request):
    return render(request, 'func_template.html')  # Рендерим func_template.html


def class_temp(request):
    return render(request, 'class_template.html')  # Рендерим class_template.html

