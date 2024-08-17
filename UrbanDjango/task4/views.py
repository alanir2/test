from django.shortcuts import render



def index(request):
    context = {

        'games': ['Atomic Heart', "Cyberpunk 2077", 'PayDay 2']
    }
    return render(request, 'fourth_task/platform.html', context)

def categories(request):
    context = {
        'games': ['Atomic Heart', "Cyberpunk 2077", 'PayDay 2']
    }

    return render(request, 'fourth_task/games.html', context)

def platform(request):

    # context = {
    #
    #     'games': ['Atomic Heart', "Cyberpunk 2077", 'PayDay 2']
    # }

    return render(request,'fourth_task/cart.html')
