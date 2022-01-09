from django.db import models

# Create your models here.

class Homepage(models.Model):
	homepage_image = models.ImageField(upload_to='homepage_images/')
	homepage_text = models.CharField(max_length=300)
