from django.db import models

# Tasks Model

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #  View each task table record using title

    def __str__(self):
        return self.title