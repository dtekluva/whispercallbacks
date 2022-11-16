from django.db import models


# Create your model(s) here.
class DotgoCallback(models.Model):
    sender_id = models.CharField(max_length=2200)
    sms_id = models.CharField(max_length=2200)
    price = models.CharField(max_length=2200)
    account_balance = models.CharField(max_length=2200)
    raw_status = models.CharField(max_length=2200)
    ref_id = models.CharField(max_length=2200)
    raw_data = models.CharField(max_length=2200)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_date_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_created"]


class RouteCallback(models.Model):
    data = models.TextField()
    description = models.CharField(max_length=2200)
    status = models.CharField(max_length=2200)
    sender_id = models.CharField(max_length=2200)
    bulkId = models.CharField(max_length=2200)
    price = models.CharField(max_length=2200)
    account_balance = models.CharField(max_length=2200)
    timestamp = models.CharField(max_length=2200)
    event_timestamp = models.CharField(max_length=2200)
    sms_id = models.CharField(max_length=2200)
    ref_id = models.CharField(max_length=2200)
    to = models.CharField(max_length=2200)
    source = models.CharField(max_length=2200)
    raw_status = models.CharField(max_length=2200)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_date_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_created"]
