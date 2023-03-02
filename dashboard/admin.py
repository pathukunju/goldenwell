
# """Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User,Store,Local,Tax,Coins,OrderStatus,StockStatus,Social,Role


admin.site.register(Store),
admin.site.register(Local),
admin.site.register(Tax),
admin.site.register(Coins),
admin.site.register(OrderStatus),
admin.site.register(StockStatus),
admin.site.register(Social),
admin.site.register(Role)

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password','role','full_name')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff','role','full_name',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)