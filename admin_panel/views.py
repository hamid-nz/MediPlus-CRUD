from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from . import views
from django.views.generic import(
    TemplateView,
    CreateView, 
    ListView,
    UpdateView,
    DeleteView
) 
from .models import Page, HomePageContent, Appointment

def AdminHome(request):
    return render(request, 'admin_panel/base.html')

class CreatePage(CreateView):
    template_name= 'admin_panel/add-page.html'
    model = Page
    fields= '__all__'
    success_url = reverse_lazy('pages-list')
    
class ListPage(ListView):
    model= Page
    template_name= 'admin_panel/list-page.html'
    # page_object_list= 'pages_list'
    
    def get(self, request):
        pages = Page.objects.all()
        my_dict = {
            'pages': pages
        }
        return render(request, 'admin_panel/list-page.html', my_dict )

class DeletePage(DeleteView):
    model = Page
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('pages-list')
    template_name= 'admin_panel/delete-page.html'
    
class EditPage(UpdateView):
    model= Page
    template_name= 'admin_panel/edit-page.html'
    fields= '__all__'   
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('pages-list')

# --------HomePage Content----------
class HomeList(ListView):
    model= HomePageContent 
    template_name= 'admin_panel/list.html'
    
    def get(self, request):
        home = HomePageContent.objects.all()
        my_dict = {
            'home': home
        }
        return render(request, 'admin_panel/list.html', my_dict )
 
class HomeCreate(CreateView):
    template_name= 'admin_panel/add.html'
    model = HomePageContent
    fields= '__all__'
    success_url = reverse_lazy('list')

class HomeEdit(UpdateView):
    model= HomePageContent
    template_name= 'admin_panel/edit.html'
    fields= '__all__'   
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('list')

#--------------- Appointment---------------------  
class ListAppointment(ListView):
    model= Appointment 
    template_name= 'admin_panel/list-appointment.html'
    
    def get(self, request):
        appointments = Appointment.objects.all()
        my_dict = {
            'appointments': appointments
        }
        return render(request, 'admin_panel/list-appointment.html', my_dict )
    
class CreateAppointment(CreateView):
    template_name= 'admin_panel/add-appointment.html'
    model = Appointment
    fields= '__all__'
    success_url = reverse_lazy('appointment-list')
    
class EditAppointment(UpdateView):
    model= Appointment
    template_name= 'admin_panel/edit-appointment.html'
    fields= '__all__'   
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('appointment-list')
    
class DeleteAppointment(DeleteView):
    model = Appointment
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('appointment-list')
    template_name= 'admin_panel/delete-appointment.html'