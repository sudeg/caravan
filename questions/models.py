from django.db import models
import uuid
from django.utils import timezone


class Question(models.Model):

    questionId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    questionEntryDate = models.DateTimeField()
    questionContent = models.TextField(blank=True, null=True, max_length=250)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
