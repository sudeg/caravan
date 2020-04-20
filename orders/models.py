from django.db import models
from django.utils import timezone
import uuid


class Order(models.Model):

    orderId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    orderStartDate = models.DateTimeField()
    orderEndDate = models.DateTimeField()
