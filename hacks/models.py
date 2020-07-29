from django.db import models

class Hack(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='homepage/images/',blank = True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

