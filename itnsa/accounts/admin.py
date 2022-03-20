from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import User

# Register your models here.

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ['username', 'password']}),
        (('Personal info'), {"fields": ['real_name', 'email', 'phone_number', 'is_student', 'is_coach', 'is_competitor']}),
        (('Permissions'), {"fields": ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}),
    )
    list_display = ('username', 'real_name', 'email', 'phone_number', 'is_student', 'is_coach', 'is_competitor') 

    def get_queryset(self, request):
        qs = super(MyUserAdmin, self).get_queryset(request)
        if request.user.is_student:
            return qs.filter(username=request.user)
        return qs


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
# admin.site.register(Group, GroupAdmin)


