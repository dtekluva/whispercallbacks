from import_export import resources

from callbacks import models


# Register your resource(s) here.
class ExchangeTelecomDlrResource(resources.ModelResource):
    class Meta:
        model = models.ExchangeTelecomDlr


class MessageStatusResource(resources.ModelResource):
    class Meta:
        model = models.MessageStatus


class UserProfileResource(resources.ModelResource):
    class Meta:
        model = models.User
