from django.urls import path
from . import views
from .views import Home, Contact, ListPage

urlpatterns = [
    path('', Home.as_view() ),
    path('contact/', Contact.as_view() ),
    path('list/', ListPage.as_view() ),
    path('page/<slug:url>/', views.PageDetail, name='page-detail'),


]
