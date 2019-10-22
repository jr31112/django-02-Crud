from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from django.contrib.auth.admin import UserAdmin

from .models import User
# Register your models here.
admin.site.register(User, UserAdmin)
>>>>>>> 595f42d1232b1f26e9e8049182029062cdf2ac10
