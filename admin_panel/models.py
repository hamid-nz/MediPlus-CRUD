from django.db import models
from django.utils import timezone

class Page(models.Model):
    #pk
    title= models.CharField('page_title', max_length=100)
    discription= models.CharField('page_discription', max_length=500 , blank=True)
    discriptive_image= models.ImageField(upload_to='img/', blank=True)
    h2= models.CharField('heading 2', max_length=100, blank=True)
    content= models.CharField('content', max_length=500, blank=True)
    h3= models.CharField('heading 3', max_length=100, blank=True)
    h4= models.CharField('heading 4', max_length=100, blank=True)
    second_content= models.CharField('second content', max_length=500, blank=True)
    image= models.ImageField(upload_to='img/', blank=True, default='')
    url= models.CharField('Slug', max_length=100)
    published_date= models.DateTimeField(default=timezone.now() )
       
    def __str__ (self):
        return self.title
    
# -----------------------------------------------HOME PAGE CMS--------------------------------------------------
class HomePageContent(models.Model):
    #pk
    title= models.CharField('Site Title', max_length=100)
    discription= models.CharField('Site Discription', max_length=500 , blank=True)  
    #Slider 1
    heading_slider_1= models.CharField('Heading Slider 1', max_length=100, blank=True)
    text_slider_1= models.CharField('text slider 1', max_length=500 , blank=True)  
    #Slider 2
    heading_slider_2= models.CharField('Heading Slider 2', max_length=100, blank=True)
    text_slider_2= models.CharField('text slider 2', max_length=500 , blank=True)  
    #Slider 3
    heading_slider_3= models.CharField('Heading Slider 3', max_length=100, blank=True)
    text_slider_3= models.CharField('text slider 3', max_length=500 , blank=True)  
    #Optional content  
    page_content_1= models.CharField('Content Box 1', max_length=1000 , blank=True)    
    page_content_2= models.CharField('Content Box 2', max_length=1000 , blank=True) 
    
    #TopCards_1
    doctor_name_1= models.CharField('Doctors Name', max_length=100, blank=True)
    title_1= models.CharField('card title', max_length=100, blank=True) 
    discription_1= models.CharField('Discription [short]', max_length=100, blank=True)
    DAYS_TYPE = {
         "Monday":"Mon",
         "Tuesday":"Tue",
         "Wednesday":"Wed",
         "Thursday":"Thurs",
         "Friday":"Fri",
         "Saturday":"Sat",
         "Sunday":"Sun",
     }
    HOURS_TYPE = {
         "9:00 AM": "9",
         "10:00 AM":"10",
         "11:00 AM":"11",
         "12:00 AM":"12",
         "1:00 PM":"1",
         "2:00 PM":"2",
         "3:00 PM":"3",
         "4:00 PM":"4",
         "5:00 PM":"5",
         "6:00 PM":"6",
     }     
    working_day_from_1 = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
    working_day_to_1 = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
    working_hour_from_1 = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
    working_hour_to_1 = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
    
    #TopCards_2
    doctor_name_2= models.CharField('Doctors Name', max_length=100, blank=True)
    title_2= models.CharField('card title', max_length=100, blank=True) 
    discription_2= models.CharField('Discription [short]', max_length=100, blank=True)
    DAYS_TYPE = {
         "Monday":"Mon",
         "Tuesday":"Tue",
         "Wednesday":"Wed",
         "Thursday":"Thurs",
         "Friday":"Fri",
         "Saturday":"Sat",
         "Sunday":"Sun",
     }
    HOURS_TYPE = {
         "9:00 AM": "9",
         "10:00 AM":"10",
         "11:00 AM":"11",
         "12:00 AM":"12",
         "1:00 PM":"1",
         "2:00 PM":"2",
         "3:00 PM":"3",
         "4:00 PM":"4",
         "5:00 PM":"5",
         "6:00 PM":"6",
     }     
    working_day_from_2 = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
    working_day_to_2 = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
    working_hour_from_2 = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
    working_hour_to_2 = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
    #TopCards3
    doctor_name_3= models.CharField('Doctors Name', max_length=100, blank=True)
    title_3= models.CharField('card title', max_length=100, blank=True) 
    discription_3= models.CharField('Discription [short]', max_length=100, blank=True)
    DAYS_TYPE = {
         "Monday":"Mon",
         "Tuesday":"Tue",
         "Wednesday":"Wed",
         "Thursday":"Thurs",
         "Friday":"Fri",
         "Saturday":"Sat",
         "Sunday":"Sun",
     }
    HOURS_TYPE = {
         "9:00 AM": "9",
         "10:00 AM":"10",
         "11:00 AM":"11",
         "12:00 AM":"12",
         "1:00 PM":"1",
         "2:00 PM":"2",
         "3:00 PM":"3",
         "4:00 PM":"4",
         "5:00 PM":"5",
         "6:00 PM":"6",
     }
    working_day_from_3 = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
    working_day_to_3 = models.CharField(blank=True, choices=DAYS_TYPE, max_length=10)
    working_hour_from_3 = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
    working_hour_to_3 = models.CharField(blank=True, choices=HOURS_TYPE, max_length=10)
    
    #Help Section 1  
    help_box_1_h5= models.CharField('Help Box 1 Heading', max_length=100, default="")    
    help_box_1= models.CharField('Help Box 1', max_length=400, default="") 
    #Help Section 2  
    help_box_2_h5= models.CharField('Help Box 2 Heading', max_length=100, default="")    
    help_box_2= models.CharField('Help Box 2', max_length=400, default="") 
    #Help Section 3  
    help_box_3_h5= models.CharField('Help Box 3 Heading', max_length=100, default="")    
    help_box_3= models.CharField('Help Box 3', max_length=400, default="") 
    #Hospital Info (homepage)   
    hospital_rooms= models.CharField('Hospital Rooms', max_length=100 )    
    specialist_doctors= models.CharField('Specialist Doctors', max_length=100 )    
    happy_patient= models.CharField('Happy Patients', max_length=100)    
    years_of_experience= models.CharField('Years of Experience', max_length=100)
    #About content on home page  
    about_h3= models.CharField('3rd Heading', max_length=100 , blank=True)    
    about_content= models.CharField('About content', max_length=1000 , blank=True)
    #emergency section
    emergency_section_h3= models.CharField('Emergency section heading', max_length=100 , blank=True) 
    emergency_section_content= models.CharField('Emergency section content', max_length=1000 , blank=True) 
    #Feature Service Batch - 1  
    batch_1_heading= models.CharField('batch 1 heading', max_length=100 , blank=True) 
    batch_1_price= models.CharField('batch 1 price', max_length=100 , blank=True) 
    batch_1_content= models.CharField('batch 1 content', max_length=1000 , blank=True) 
    #Feature Service Batch - 2  
    batch_2_heading= models.CharField('batch 2 heading', max_length=100 , blank=True) 
    batch_2_price= models.CharField('batch 2 price', max_length=100 , blank=True) 
    batch_2_content= models.CharField('batch 2 content', max_length=1000 , blank=True) 
    #Feature Service Batch - 3  
    batch_3_heading= models.CharField('batch 3 heading', max_length=100 , blank=True) 
    batch_3_price= models.CharField('batch 3 price', max_length=100 , blank=True) 
    batch_3_content= models.CharField('batch 3 content', max_length=1000 , blank=True) 
    #Social Links 
    facebook= models.CharField('facebook link', max_length=1000 , blank=True) 
    google= models.CharField('google +', max_length=1000 , blank=True) 
    twitter= models.CharField('twitter link', max_length=1000 , blank=True) 
    linkedin= models.CharField('linkedin link', max_length=1000 , blank=True) 
    pinterest= models.CharField('pinterest link', max_length=1000 , blank=True) 
    
    
    def __str__ (self):
         return self.title
    
class Appointment(models.Model):
    #pk
    name= models.CharField('Name', max_length=100, blank=True)
    email= models.EmailField('E Mail', max_length=100, default="")
    phone= models.IntegerField('Phone', max_length=11, default="")
    DEPARTMENT = {
        "Dentistry": "dentistry",
        "Crdiology": "cardiology",
        "Childrens": "childrens",
        "Pet Care": "pet care",
        "OPD": "opd", 
     }
    # published_date= models.DateTimeField(default="")
    department = models.CharField(choices=DEPARTMENT, max_length=10)
    message = models.CharField('Your Message', max_length=500, blank=True)
    
    def __str__ (self):
         return self.name