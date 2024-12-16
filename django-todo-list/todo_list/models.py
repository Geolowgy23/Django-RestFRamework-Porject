from django.db import models

class List(models.Model):
    item = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return self.item
