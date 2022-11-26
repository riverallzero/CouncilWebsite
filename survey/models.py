from django.db import models


# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject