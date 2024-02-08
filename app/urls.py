from django.urls import path
from . import views
from .views import Home, Contact, ListPage, ScheduleAppointment

urlpatterns = [
    path('', Home.as_view() ),
    path('contact/', Contact.as_view() ),
    path('appointment/', ScheduleAppointment.as_view() ),
    path('treatment/<slug:url>/', views.PageDetail, name='page-detail'),
    
    
    #Remove after complete development
    path('base/', ListPage.as_view() ),
]
