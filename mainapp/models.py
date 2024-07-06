
from django.db import models
from django.utils import timezone


class SessionUrl(models.Model):
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class Session(models.Model):
    session_id = models.CharField(max_length=40, primary_key=True)
    session_url = models.ForeignKey(SessionUrl, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    @classmethod
    def create_or_update_session(cls, session_key):
        """
        Метод вызывается из class HomePage def dispatch и записывает в таблицу session_key в колонку session_id.
        Тут нужно что-то еще сделать с session_url, которая указывает на таблицу SessionUrl, иначе выходит ошибка
        NOT NULL constraint failed: mainapp_session.session_url_id
        """
        session, created = cls.objects.get_or_create(session_id=session_key)
        return session

    def __str__(self):
        return self.session_id
