
from django.db import models
from django.utils import timezone


class Session(models.Model):
    key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class SessionUrl(models.Model):
    url = models.CharField(max_length=40)
    session_key = models.ForeignKey(Session, on_delete=models.CASCADE)
