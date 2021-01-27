from django.db import models

# Create your models here.


class Snippet(models.Model):
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.fname
