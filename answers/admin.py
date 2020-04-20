from django.contrib import admin

# ekleme,düzenleme,silme tarzı işlemler için burayı kullanacağız.

from .models import Answer

admin.site.register(Answer)
