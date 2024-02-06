from django.urls import path
from . import views
from .views import (
    CreatePage, 
    ListPage,
    EditPage,
    DeletePage,
    ListCard 
)
urlpatterns = [
    path('', views.AdminHome, name='AdminHome'),
    path('add-page/', CreatePage.as_view() , name='add-page'),
    path('pages/', ListPage.as_view() , name='pages-list'),
    path('edit/<int:pk>/', EditPage.as_view() , name='edit-page'),
    path('delete/<int:pk>/', DeletePage.as_view() , name='delete-page'),
    path('card/', ListCard.as_view() , name='card-list'),
]

