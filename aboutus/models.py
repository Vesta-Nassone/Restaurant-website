from django.db import models

# Create your models here.
class AboutUs(models.Model):
    tittle = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

class WhyChooseUs(models.Model):
    title = ""
    content = ""

class Chefs(models.Model):
    name = ""
    subtitle = ""
    image = ""