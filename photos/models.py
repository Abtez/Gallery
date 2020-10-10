from django.db import models

class location(models.Model):
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
    tags = models.ManyToManyField(location)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default='')
    
    def __str__(self):
        return self.first_name
    
    def save_image(self):
        self.save()
        
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos
        
    