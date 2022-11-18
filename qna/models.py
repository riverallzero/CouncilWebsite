from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Qna(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField(blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    command = models.TextField(blank=True)

    def __str__(self):
        return f'{self.pk}:{self.title}'

    def get_absolute_url(self):
        return f'/qna/{self.pk}/'
