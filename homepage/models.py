from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='homepage/images/',blank = True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    skillpercentage = models.DecimalField(max_digits = 3, decimal_places = 0)

    def __str__(self):
        return self.skill

