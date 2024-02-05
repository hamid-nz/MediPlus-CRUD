from django.shortcuts import render, HttpResponse
from django.urls import reverse
from admin_panel.models import Page
from django.views.generic import(
    TemplateView,
    CreateView, 
    ListView,
    UpdateView,
    DeleteView
    )

# Create your views here.


class Home(TemplateView):
    template_name = 'app/home.html'
    
class Contact(TemplateView):
    template_name = 'app/contact.html'
    
    
class ListPage(ListView):
    model= Page
    template_name = 'app/base.html'


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