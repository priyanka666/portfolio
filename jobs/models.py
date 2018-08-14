from django.db import models

# Create your models here.
class Jobs(model.Model):
    image = models.ImageField(upload_to='/image')