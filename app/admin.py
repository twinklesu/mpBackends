from django.contrib import admin
from .models import Test, UserInfo, Pet

# Register your models here.
admin.site.register(Test)
admin.site.register(UserInfo)
admin.site.register(Pet)