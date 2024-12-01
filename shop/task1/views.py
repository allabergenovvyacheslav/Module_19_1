from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegister
from .models import Buyer, Game


# Create your views here.


def registration_page(request):
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            context = {'info': info, 'form': form}

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=0.0)
                return HttpResponse(f'Приветствую, {username}!')
            return render(request, 'registration_page.html', context)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def platform(request):
    title = 'World of oak flooring'
    text = 'Home page'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'platform.html', context)


def products(request):
    text_prod = 'Company products'
    production = Game.objects.all()
    text_buy = 'Choose'
    text_back = 'Go back'
    context = {
        'text_prod': text_prod,
        'production': production,
        'text_buy': text_buy,
        'text_back': text_back,
    }
    return render(request, 'products.html', context)


def cart(request):
    text_cart = 'Your choice of products:'
    your_choice = 'Sorry, your cart is empty'
    text_back = 'Go back'
    context = {
        "text_cart": text_cart,
        'your_choice': your_choice,
        'text_back': text_back,
    }
    return render(request, 'cart.html', context)
