from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from callbacks.models import (
    ExchangeTelecomDlr,
    User
)


# Register your model(s) here.
class ExchangeTelecomDlrResource(resources.ModelResource):

    class Meta:
        model = ExchangeTelecomDlr


class UserProfileResource(resources.ModelResource):

    class Meta:
        model = User


class ExchangeTelecomDlrResourceAdmin(ImportExportModelAdmin):
    resource_class = ExchangeTelecomDlrResource
    search_fields = []
    list_filter = ()
    date_hierarchy = "created_at"

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


class UserProfileResourceAdmin(ImportExportModelAdmin):
    resource_class = UserProfileResource
    search_fields = []
    list_filter = ()
    date_hierarchy = "created_at"

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


admin.site.register(ExchangeTelecomDlr, ExchangeTelecomDlrResourceAdmin)
admin.site.register(User, UserProfileResourceAdmin)
