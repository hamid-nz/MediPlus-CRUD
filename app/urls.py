from django.urls import path
from . import views
from .views import Home, Contact, ListPage

urlpatterns = [
    path('', Home.as_view() ),
    path('contact/', Contact.as_view() ),
    path('treatment/<slug:url>/', views.PageDetail, name='page-detail'),
    
    
    #Remove after complete development
    path('list/', ListPage.as_view() ),
]
