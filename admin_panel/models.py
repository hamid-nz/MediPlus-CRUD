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
    image= models.ImageField(upload_to='img/', blank=True, default='')
    url= models.CharField('Slug', max_length=100)
    published_date= models.DateTimeField(default=timezone.now() )
    
    class Meta:
        # data_table = 'pages'
        pass     
    def __str__ (self):
        return self.title

class TopCard(models.Model):
     #pk
     Doctor_name= models.CharField('card text', max_length=100)
     title= models.CharField('card title', max_length=100) 
     discription= models.CharField('Discription [short]', max_length=100)
     DAYS_TYPE = {
         "A": "Monday",
         "B": "Tuesday",
         "C": "Wednesday",
         "D": "Thursday",
         "E": "Friday",
         "F": "Saturday",
         "G": "Sunday"
     }
     HOURS_TYPE = {
         "9:00 AM": "A",
         "B": "10:00 AM",
         "C": "11:00 AM",
         "D": "12:00 AM",
         "E": "1:00 PM",
         "F": "2:00 PM",
         "G": "3:00 PM",
         "H": "4:00 PM",
         "I": "5:00 PM",
         "J": "6:00 PM",
     }
     
     working_day_from = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
     working_day_to = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
     working_hour_from = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
     working_hour_to = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
     def __str__ (self):
         return self.title
    
    
