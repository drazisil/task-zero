from django.db import models

class Task(models.Model):
    timestamp = models.DateTimeField('date created')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
