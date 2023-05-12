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


class ExchangeTelecomDlr(BaseModel):
    payload = models.TextField()

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ["-created_at"]
