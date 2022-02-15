from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    
    def __str__(self):
        return self.title