from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from game_setup.models import Game, Guess


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
    if request.method == 'POST':
        guess_value = request.POST['user-guess']
        new_guess = Guess.objects.create(guess_value=guess_value, game=current_game)
        if new_guess.guess_value not in current_game.winning_word:
            current_game.attempts_left -= 1
            current_game.save()
    all_guesses = Guess.objects.filter(game=current_game)
    context = {
        'game': current_game,
        'guesses': all_guesses
        }
<<<<<<< HEAD
    return render(request, 'single_game.html', context)
=======
    return render(request, 'single_game.html', context)
>>>>>>> 5c2a1bd7cf363b18797e90601f4019d95faa829d
