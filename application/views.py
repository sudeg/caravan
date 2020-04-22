from django.shortcuts import render

from .models import Answer, Order, Product, Profile, Question

from django.utils import timezone

from .forms import AnswerForm, OrderForm, ProductForm, ProfileForm, QuestionForm, UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def answers_list(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AnswerForm()
    context = {
        'form': form
    }
    return render(request, "application/answers_list.html", context)


def orders_list(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, "application/orders_list.html", context)


def products_list(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "application/products_list.html", context)


def profiles_list(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, "application/profiles_list.html", context)


def questions_list(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, "application/questions_list.html", context)


def index(request):
    return render(request, 'application/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'application/registration.html',
                  {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'application/login.html', {})


@login_required
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'application/profile.html', {'profile_user': user})
