from django.contrib import admin

from products.admin import BasketAdmin
from users.models import User, EmailVerification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_verified_email',)
    list_editable = ('is_verified_email',)

    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'created', 'expiration')
    readonly_fields = ('created',)
