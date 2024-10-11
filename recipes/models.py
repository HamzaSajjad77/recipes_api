from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()  
    instructions = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)  
    area = models.CharField(max_length=100, null=True, blank=True)  
    image_url = models.URLField(null=True, blank=True) 
    video_url = models.URLField(null=True, blank=True) 
    source_url = models.URLField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title