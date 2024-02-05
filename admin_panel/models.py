from django.db import models
from tinymce.models import HTMLField
# from datetime import datetime


class Page(models.Model):
    #pk
    page_title= models.CharField('page_title', max_length=100)
    page_discription= models.CharField('page_discription', max_length=500)
    page_content= HTMLField()
    page_url= models.CharField('Slug', max_length=100, default='' )
    # page_image= models.ImageField(upload_to='img/',)
    
    class Meta:
        # data_table = 'pages'
        pass
        
    def __str__ (self):
        return self.page_title