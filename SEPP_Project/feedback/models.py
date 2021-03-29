from django.db import models

# Create your models here.
class Feedback(models.Model):
    Uname = models.CharField(max_length=25)
    Feedback = models.CharField(max_length=255)