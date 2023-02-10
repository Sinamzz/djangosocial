from django.contrib import admin
from .models import Relation, Profile, IpLog, IpAddress
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class IpAddressInline(admin.StackedInline):
    model = IpAddress
    can_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileInline, IpAddressInline)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
admin.site.register(Relation)
admin.site.register(IpLog)
admin.site.register(IpAddress)
