from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy, reverse

from django.urls import reverse
from admin_panel.models import Page, HomePageContent, Appointment
from django.views.generic import(
    TemplateView,
    CreateView, 
    ListView,
    UpdateView,
    DeleteView
    )

# Create your views here.

class Home(ListView):
    model= HomePageContent, Page 
    
    def get(self, request):
        homepagecontent = HomePageContent.objects.all()
        pages = Page.objects.all()
        template_names = [
        'app/home.html', 
        'app/base.html', 
        ]
        my_dict = {
            'homepagecontent': homepagecontent,
            'pages': pages
        }
        return render(request, 'app/home.html', my_dict )
class Contact(TemplateView):
    template_name = 'app/contact.html'
      

class ScheduleAppointment(CreateView):
    model= Appointment
    fields="__all__"
    template_name = 'app/book-appointment.html'
    success_url = reverse_lazy('appointment-list')

#Used Functional views for single detail page
def PageDetail(request, url):
    pagedetail= Page.objects.get(url=url)
    pages = Page.objects.all()
    my_dict_data= {
        'pagedetail': pagedetail,
        'pages': pages, 
        
    }
    # Render the view to multiple templates
    template_names = [
        'app/single-page.html', 
        'app/base.html'
        ]
    print(pagedetail)  
    return render(request, template_names , my_dict_data )
