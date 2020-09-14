from django.contrib import admin
from .models import RegisterUser


class RegUser(admin.ModelAdmin):
    list_display = [
        "user", "first_name", "last_name", "email"
    ]


admin.site.register(RegisterUser, RegUser)
