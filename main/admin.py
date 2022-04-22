from django.contrib import admin

#추가
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=(
        
    )
admin.site.register(User,UserAdmin)