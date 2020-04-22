from django import forms

from .models import Answer, Order, Product, Profile, Question

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = [
            'replyEntryDate',
            'replyContent'
        ]


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'orderStartDate',
            'orderEndDate'
        ]


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'productType',
            'productName',
            'productVerification',
            'productLicense',
            'createDate'
        ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'portfolio_site',
            'profile_pic',
        ]


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'questionEntryDate',
            'questionContent'
        ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')

