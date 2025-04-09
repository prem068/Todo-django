from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500,null=True, blank=True, default=None)
    due_date = models.DateField()
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title