from django.contrib import admin
from accounts.models import User, Session

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'firstname',
        'lastname',
        'last_login',
    )
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('-last_login',)

admin.site.register(Session)