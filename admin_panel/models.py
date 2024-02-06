from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
# from datetime import datetime


class Page(models.Model):
    #pk
    title= models.CharField('page_title', max_length=100)
    discription= models.CharField('page_discription', max_length=500 , blank=True)
    discriptive_image= models.ImageField(upload_to='img/', blank=True)
    h2= models.CharField('heading 2', max_length=100, blank=True)
    content= HTMLField(blank=True)
    h3= models.CharField('heading 3', max_length=100, blank=True)
    h4= models.CharField('heading 4', max_length=100, blank=True)
    second_content= HTMLField( blank=True)
    image= models.ImageField(upload_to='img/', default='')
    url= models.CharField('Slug', max_length=100)
    published_date= models.DateTimeField(default=timezone.now() )
    
    class Meta:
        # data_table = 'pages'
        pass
        
    def __str__ (self):
        return self.title