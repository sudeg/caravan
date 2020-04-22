from django.contrib import admin

from .models import Answer
from .models import Order
from .models import Product
from .models import Profile
from .models import Question
from .models import User

admin.site.register(Answer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Question)
