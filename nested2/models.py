from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    
    def __str__(self):
        return self.title
    
class scrapped_data(models.Model):
    article_num = models.IntegerField()
    article_title = models.CharField(45)
    article_authors = models.CharField(45)
    article_date = models.DateField()
    article_link = models.TextField()
    article_IMG = models.TextField()
    article_pol = models.CharField(20)
    article_subj = models.CharField(20)
    article_summ = models.TextField()