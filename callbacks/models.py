import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


# Create your model(s) here.
class BaseModel(models.Model):
    """Base model for reuse.
    Args:
        models (Model): Django's model class.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        _('date created'), auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(
        _('date updated'), auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    pass

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "USER PROFILE"
        verbose_name_plural = "USER PROFILES"


class ExchangeTelecomDlr(BaseModel):
    """
    Exchange Telecom Messages DLR's.
    """
    message_id = models.CharField(max_length=125)
    message_service = models.CharField(max_length=125, null=True, blank=True)
    external_id = models.CharField(max_length=125)
    recipient = models.CharField(max_length=125)
    message_status = models.CharField(max_length=125)
    payload = models.TextField()

    def __str__(self) -> str:
        return self.recipient

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "EXCHANGE TELECOM DLR"
        verbose_name_plural = "EXCHANGE TELECOM DLRS"


class MessageStatus(BaseModel):
    device_provider = models.CharField(max_length=2300, null=True, blank=True)
    account_balance = models.CharField(max_length=2200)
    event_timestamp = models.CharField(max_length=2200)
    sender_id = models.CharField(max_length=2200)
    timestamp = models.CharField(max_length=2200)
    raw_status = models.TextField(max_length=3000, default="")
    sms_id = models.CharField(max_length=2200)
    ref_id = models.CharField(max_length=2200)
    status = models.CharField(max_length=2200)
    price = models.CharField(max_length=2200)
    to = models.CharField(max_length=2200)
    source = models.CharField(max_length=20, default="DOTGO")
    route_updated = models.BooleanField(default=False)
    dlr_push_count = models.IntegerField(default=0)
    dlr_response = models.CharField(max_length=10, default=0)
    dlr_status_code = models.CharField(max_length=10, default=0)
    updated_date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.to

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "MESSAGE STATUS"
        verbose_name_plural = "MESSAGE STATUSES"
