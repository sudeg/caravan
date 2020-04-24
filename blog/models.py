from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField(null=True)  # lokasyon
    capacity = models.IntegerField(null=True)  # karavan kapasitesi
    rentPricePerDay = models.IntegerField(null=True)  # günlük kiralama bedeli

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    title = models.CharField(max_length=100)  # karavan adı
    content = models.TextField()  # brief explanation
    date_posted = models.DateTimeField(
        default=timezone.now)  # sisteme eklenme tarihi
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ekleyen kişi
    location = models.TextField()  # lokasyon
    capacity = models.IntegerField()  # karavan kapasitesi
    rentPricePerDay = models.IntegerField()  # günlük kiralama bedeli

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
