from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


class Answer(models.Model):

    answerId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    replyEntryDate = models.DateTimeField()
    replyContent = models.TextField(blank=True, null=True, max_length=250)


class Order(models.Model):

    orderId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    orderStartDate = models.DateTimeField()
    orderEndDate = models.DateTimeField()


class Product(models.Model):
    ProductId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    productType = models.TextField(blank=True, null=True)
    productName = models.TextField(blank=False, null=False)
    productVerification = models.BooleanField(default=False)
    productLicense = models.TextField(blank=True, null=True)
    createDate = models.DateTimeField()


class Question(models.Model):

    questionId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    questionEntryDate = models.DateTimeField()
    questionContent = models.TextField(blank=True, null=True, max_length=250)


class Profile(models.Model):
    profileId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)

    email = models.EmailField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    lastName = models.TextField(blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    productAmount = models.IntegerField(blank=True, null=True)
    rentedProductAmount = models.IntegerField(blank=True, null=True)


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
