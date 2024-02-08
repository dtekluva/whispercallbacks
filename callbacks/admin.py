from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from . import models, resources


# Register your model(s) here.
class ExchangeTelecomDlrResourceAdmin(ImportExportModelAdmin):
    resource_class = resources.ExchangeTelecomDlrResource
    search_fields = [
        "external_id",
        "recipient"
    ]
    list_filter = ("message_service", "message_status")
    date_hierarchy = "created_at"

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


class MessageStatusResourceAdmin(ImportExportModelAdmin):
    resource_class = resources.MessageStatusResource
    search_fields = [
        "ref_id",
        "to"
    ]
    list_filter = ()
    date_hierarchy = "created_at"

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


class UserProfileResourceAdmin(ImportExportModelAdmin):
    resource_class = resources.UserProfileResource
    search_fields = []
    list_filter = ()
    date_hierarchy = "created_at"

    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


admin.site.register(models.ExchangeTelecomDlr, ExchangeTelecomDlrResourceAdmin)
admin.site.register(models.MessageStatus, MessageStatusResourceAdmin)
admin.site.register(models.User, UserProfileResourceAdmin)
