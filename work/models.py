from django.db import models

# Create your models here.

class Work(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

def __repr__(self):
    return self.title