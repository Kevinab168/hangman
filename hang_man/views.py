from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from game_setup.models import Game


def homepage(request):
    return render(request, 'index.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('play_game')
    else:
        return render(request, 'log_in.html')


def play_game(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
        new_game = Game.objects.create(user=current_user)
        return redirect('single_game', new_game.pk)
    return render(request, 'play_game.html')


def game(request, game_id):
    current_game = Game.objects.all().get(pk=game_id)
    context = {'game': current_game}
    return render(request, 'single_game.html', context)