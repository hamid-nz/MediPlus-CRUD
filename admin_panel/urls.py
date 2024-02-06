from django.urls import path
from . import views
from .views import (
    CreatePage, 
    ListPage,
    EditPage,
    DeletePage,
    ListView, 
    CreateView
)
urlpatterns = [
    path('', views.AdminHome, name='AdminHome'),
    path('add-page/', CreatePage.as_view() , name='add-page'),
    path('pages/', ListPage.as_view() , name='pages-list'),
    path('edit-page/<int:pk>/', EditPage.as_view() , name='edit-page'),
    path('delete-page/<int:pk>/', DeletePage.as_view() , name='delete-page'),
    path('list/', ListView.as_view() , name='list'),
    path('add/', CreateView.as_view() , name='add'),

]

