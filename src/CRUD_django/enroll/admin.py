from django.contrib import admin
from .models import User
# Register your models here.

# admin.site.register(User)

# or

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
