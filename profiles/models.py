
from django.db import models

import uuid


class Profile(models.Model):
    profileId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)

    email = models.EmailField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    lastName = models.TextField(blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    productAmount = models.IntegerField(blank=True, null=True)
    rentedProductAmount = models.IntegerField(blank=True, null=True)
