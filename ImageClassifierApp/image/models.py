from django.db import models

# Create your models here.

class Image(models.Model):

    image = models.ImageField(null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'image'