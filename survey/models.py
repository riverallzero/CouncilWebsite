from django.db import models

# Create your models here.

class Survey(models.Model):
    subject = models.CharField(max_length=15, blank=True)
    title = models.CharField(max_length=50)
    describe = models.TextField(blank=True)
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject}:{self.title}'


    def get_absolute_url(self):
        return f'/survey/{self.pk}/'