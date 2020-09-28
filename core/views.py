from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login


def profile(request):
    games = Game.objects.all()
    return render(request, 'profile.html', {'games': games})


def register_game(request):
    form = GameForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'game-form.html', {'form': form})


def update_game(request, id):
    games = Game.objects.get(id=id)
    form = GameForm(request.POST or None, instance=games)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'game-form.html', {'form': form, 'games': games})


def delete_game(request, id):
    games = Game.objects.get(id=id)

    if request.method == 'POST':
        games.delete()
        return redirect('profile')

    return render(request, 'game-delete-ok.html', {'games': games})


def my_games(request):
    games = Game.objects.filter(author=request.user)
    return render(request, 'profile.html', {'games': games})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profile')

    else:
        form = UserCreationForm()
        return render(request, 'account.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})





