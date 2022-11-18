from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}:{self.title}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'