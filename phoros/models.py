from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.TextField()
    # location = models.Foreignkey(Location)
    # category = models.ForeignKey(Category)