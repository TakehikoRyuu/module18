from django.shortcuts import render


def cart_temp(request):
    return render(request, 'fourth_task/cart.html')


def games_temp(request):
    context = {
        'games': ["Warframe", "Grand Theft Auto V", "Path of Exile"]
    }
    return render(request, 'fourth_task/games.html', context)


def platform_temp(request):
    return render(request, 'fourth_task/platform.html')


def menu_temp(request):
    return render(request, 'fourth_task/menu.html')
# Create your views here.
