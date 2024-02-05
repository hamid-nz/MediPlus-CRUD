from django.urls import path
from . import views
from .views import Home, Contact, SinglePage, ListPage

urlpatterns = [
    path('', Home.as_view() ),
    path('contact/', Contact.as_view() ),
    path('list/', ListPage.as_view() ),
    path('page/', SinglePage.as_view() ),


]
