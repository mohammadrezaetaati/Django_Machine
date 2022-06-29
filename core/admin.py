from django.contrib import admin
from core.models import Car, CarPart, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# admin.site.register(User)
admin.site.register(CarPart)


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ['email', 'role']
    fieldsets = (
        (None, {"fields": ("email", "password",'role')}),

        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser")}
        ),
        ("Important dates", {"fields": ("last_login",)})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": ("email", "password1", "password2",'role','is_active','is_staff','is_superuser')
        }),
    )


admin.site.register(User, UserAdmin)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # chia to panel namayesh bede
    list_display = ("id", "car_name", "is_repair", 'is_finished')
    # form = PostForm
    list_filter = ("is_repair", "is_finished")
    list_editable = ("is_repair", "is_finished")

    actions = ['enable_is_repair', 'enable_is_finished',
               'disable_is_repair', 'disable_is_finished']

    def enable_is_finished(self, request, queryset):
        for ele in queryset:
            ele.is_finished = True
            ele.save()

    def disable_is_finished(self, request, queryset):
        for ele in queryset:
            ele.is_finished = False
            ele.save()

    def enable_is_repair(self, request, queryset):
        for ele in queryset:
            ele.is_repair = True
            ele.save()

    def disable_is_repair(self, request, queryset):
        for ele in queryset:
            ele.is_repair = False
            ele.save()
