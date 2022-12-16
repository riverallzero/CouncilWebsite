from django.db import models


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    head_image = models.ImageField(upload_to='notice/images/%Y/%m/%d/', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject