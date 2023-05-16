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
    MESSAGE_SERVICE_CHOICES = (
        ("wprohtmt", "PROMOTIONAL"),
        ("wtrxhtmo", "TRANSACTIONAL")
    )
    MESSAGE_STATUS_CHOICES = [
        ("200", "DELIVERED"),
        ("400", "EXPIRED"),
        ("403", "DELETED"),
        ("404", "UNDELIVERED"),
        ("405", "UNKNOWN"),
        ("406", "ACCEPTED"),
        ("407", "REJECTED")

    ]
    message_id = models.CharField(max_length=125)
    message_service = models.CharField(
        max_length=125, choices=MESSAGE_SERVICE_CHOICES, null=True, blank=True
    )
    external_id = models.CharField(max_length=125)
    recipient = models.CharField(max_length=125)
    message_status = models.CharField(
        max_length=125, choices=MESSAGE_STATUS_CHOICES
    )
    payload = models.TextField()

    def __str__(self) -> str:
        return self.recipient

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "EXCHANGE TELECOM DLR"
        verbose_name_plural = "EXCHANGE TELECOM DLRS"
