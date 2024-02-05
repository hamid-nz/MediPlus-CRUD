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
from .models import Page

def AdminHome(request):
    return render(request, 'admin_panel/base.html')

class CreatePage(CreateView):
    template_name= 'admin_panel/add-page.html'
    model = Page
    fields= '__all__'
    success_url = reverse_lazy('pages-list')
    

class ListPage(ListView):
    model= Page
    template_name= 'admin_panel/pages.html'
    # page_object_list= 'pages_list'
    
    def get(self, request):
        pages = Page.objects.all()
        my_dict = {
            'pages': pages
        }
        return render(request, 'admin_panel/pages.html', my_dict )

class DeletePage(DeleteView):
    model = Page
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('pages-list')
    template_name= 'admin_panel/confirm-delete.html'
    
class EditPage(UpdateView):
    model= Page
    template_name= 'admin_panel/edit-page.html'
    fields= '__all__'   
    pk_url_kwarg= 'pk'
    success_url = reverse_lazy('pages-list')
    














# from django.views.generic import (
#     CreateView,
#     DetailView,
#     UpdateView,
#     ListView,
#     DeleteView
# )
# from django.contrib import messages
# from .forms import JobForm
# from .models import Job



# class CreateJobView(CreateView):
#     model = Job
#     form_class = JobForm

#     def form_valid(self, form):
#         messages.success(self.request, 'Job added successfully.')
#         return super().form_valid(form)


# class JobDetailView(DetailView):
#     model = Job
#     context_object_name = 'job'
#     template_name = 'admin_panel/admin.html'

#     def get(self, request, pk):
#         job = get_object_or_404(Job, pk=pk)

#         # Check for success messages and pass them to the template
#         success_messages = messages.get_messages(request)
#         success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]

#         return render(request, self.template_name, {'job': job, 'success_messages': success_messages_list})


# class EditJobView(UpdateView):
#     model = Job
#     form_class = JobForm

#     def form_valid(self, form):
#         messages.success(self.request, 'Job updated successfully.')
#         return super().form_valid(form)


# class JobListView(ListView):
#     model = Job
#     template_name = 'admin_panel/job_list.html'
#     context_object_name = 'jobs'

#     def get(self, request):
#         # Check for success messages and pass them to the template
#         success_messages = messages.get_messages(request)
#         success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]
#         jobs = Job.objects.all()

#         return render(request, self.template_name, {'jobs': jobs, 'success_messages': success_messages_list})


# class DeleteJobView(DeleteView):
#     model = Job
#     success_url = reverse_lazy('job_list')

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, 'Job deleted successfully.')
#         return super().delete(request, *args, **kwargs)