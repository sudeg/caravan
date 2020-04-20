from django.db import models
import uuid
from django.utils import timezone


class Answer(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    answerId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    replyEntryDate = models.DateTimeField()
    replyContent = models.TextField(blank=True, null=True, max_length=250)
