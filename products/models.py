from django.db import models
from django.utils import timezone

import uuid


class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ProductId = models.CharField(
        max_length=100, null=True, blank=True, default=uuid.uuid4)
    productType = models.TextField(blank=True, null=True)
    productName = models.TextField(blank=False, null=False)
    productVerification = models.BooleanField(default=False)
    productLicense = models.TextField(blank=True, null=True)
    createDate = models.DateTimeField()


#    def __str__(self):
#        return self.productType

 #   def __str__(self):
#        return self.productLicense

 #   def __str__(self):
  #      return self.productName

   # def publish(self):
    #    self.createDate = timezone.now()
    #   self.save()
