from django import forms

from .models import Answer, Order, Product, Profile, Question


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
            'email',
            'name',
            'lastName',
            'password',
            'productAmount',
            'rentedProductAmount'


        ]


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'questionEntryDate',
            'questionContent'
        ]
