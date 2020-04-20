from django.shortcuts import render

from .forms import AnswerForm, OrderForm, ProductForm, ProfileForm, QuestionForm


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
