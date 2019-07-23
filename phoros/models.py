from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length = 40)    


  def __str__(self):
    return self.name

  def save_location(self):
    self.save()

  def del_location(self):
    self.delete()

  def update_location(self):
    self.insert()


class Category(models.Model):
  name = models.CharField(max_length=70)

  def __str__(self):
    return self.name    

  def save_category(self):
    self.save()

  def del_category(self):
    self.delete()

  def update_category():
    self.insert()

  @classmethod
  def get_categories_id(cls, id):
    category = Category.objects.get(pk=id)
    return category


class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    name = models.CharField(max_length =40)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.name

    def save_image(self):
      self.save()

    def del_image(self):
      self.delete()

    def update_image(self):
      self.insert()

    @classmethod
    def search_by_category(cls,search_term):

      image_result = cls.objects.filter(category__name__icontains=search_term)
      return image_result

    @classmethod
    def filter_by_location(cls,filter_location):
      image = cls.objects.filter(location__id=filter_location)
      return image

    @classmethod
    def get_image_by_id(cls,id):
      image = cls.objects.get(id=id)
      return image

    @classmethod
    def get_all_images(cls):
      all_images = Image.objects.all()
      return all_images
