from django.db import models

# Create your models here.

class GeneratedImage(models.Model):
    prompt = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.prompt

