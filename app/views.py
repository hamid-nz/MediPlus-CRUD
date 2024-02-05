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
    def get(self, request): 
        template_names = [
        'app/base.html'
        ]
        pages = Page.objects.all()
        my_dict_data = {
            'pages': pages
        }
        return render(request, template_names , my_dict_data )

# Used Functional views for single detail page
def PageDetail(request, url):
    pagedetail= Page.objects.get(url=url)
    my_dict_data= {'pagedetail': pagedetail}
    # Render the view to multiple templates
    template_names = [
        'app/single-page.html', 
        'app/base.html'
        ]
    print(pagedetail)  
    return render(request, template_names , my_dict_data )