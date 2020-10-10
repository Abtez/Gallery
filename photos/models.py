from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    description = models.TextField()
    tag = models.ForeignKey()
    
    def __str__(self):
        return self.first_name
    
    def save_image(self):
        self.save()
        
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    