from django.shortcuts import render


def cart_temp(request):
    return render(request, 'cart.html')


def games_temp(request):
    return render(request, 'games.html')


def platform_temp(request):
    return render(request, 'platform.html')
# Create your views here.
