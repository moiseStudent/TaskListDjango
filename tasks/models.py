from django.db import models

class Task(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20) # STATUS - 1. Done, 2. To do, 3. In process 


