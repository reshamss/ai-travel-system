from django.db import models

# Create your models here.

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name


