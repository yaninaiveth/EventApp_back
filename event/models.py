from django.db import models

class EventPost(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField(max_length=144)

    def __str__(self):
        return self.name
