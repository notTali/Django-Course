from django.db import models

# Create your models here.
class notes(models.Model): #tell django that this class is a model
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    