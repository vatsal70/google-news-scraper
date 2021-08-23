from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=5000)
    url = models.CharField(max_length=5000)
    image = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.title[:100] + "..."
    
    class Meta:
        ordering = ['-title']