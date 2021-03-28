from django.db import models

# Create your models here.
class toDo(models.Model):
    user = models.CharField(max_length=50)
    task = models.TextField()
    time = models.TimeField(auto_now= True)