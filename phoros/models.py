from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(max_length =30)
    name = models.CharField(max_length =30)
    description = models.TextField()
    # location = models.Foreignkey(Location)
    # category = models.ForeignKey(Category)

    @classmethod
    def search_by_title(cls,search_term):
        image_result = cls.objects.filter(category__name__icontains=search_term)
        return image_result


class Location(models.Model):
  name = models.CharField(max_length = 30)    


  def __str__(self):
    return self.name


class Category(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name    