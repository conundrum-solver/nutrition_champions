from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('user__username', 'user__email', 'full_name')
    ordering = ('-user__date_joined',)

    def full_name(self, obj):
        return obj.user.get_full_name()

    full_name.short_description = 'Full Name'
    full_name.admin_order_field = 'user__first_name'

    def email(self, obj):
        return obj.user.email

    email.short_description = 'Email'
    email.admin_order_field = 'user__email'
