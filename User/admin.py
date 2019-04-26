from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from User.models import User
# Register your models here.

class teamform(UserAdmin):
    model=User
    fieldsets=(
        (None,{'fields':('TeamID','username','email','password')}),
        ('Extras',{'fields':('is_active','is_FirstLogin','questions_attempted')}),
        )

admin.site.unregister(Group)
admin.site.register(User,teamform)
