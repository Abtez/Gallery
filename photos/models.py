from django.db import models

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    description = models.TextField()
    location = models.ManyToManyField(Location)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default='')
    
    def __str__(self):
        return self.image_name
    
    def save_image(self):
        self.save()
        
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
        
    