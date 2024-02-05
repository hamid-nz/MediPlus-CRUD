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
    context_object_name= 'obj'
    model= Page
    template_name= 'app/list.html'

# Used Functional views for single detail page
def PageDetail(request, url):
    pagedetail= Page.objects.get(url=url)
    print(pagedetail)  
    return render(request, 'app/single-page.html', {'pagedetail': pagedetail} )
