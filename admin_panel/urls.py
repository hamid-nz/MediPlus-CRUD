from django.urls import path
from . import views
from .views import (
    CreatePage, 
    ListPage,
    EditPage,
    DeletePage,
    ListCard, 
    CreateCard,
    ListView, 
    CreateView
)
urlpatterns = [
    path('', views.AdminHome, name='AdminHome'),
    path('add-page/', CreatePage.as_view() , name='add-page'),
    path('pages/', ListPage.as_view() , name='pages-list'),
    path('edit-page/<int:pk>/', EditPage.as_view() , name='edit-page'),
    path('delete-page/<int:pk>/', DeletePage.as_view() , name='delete-page'),
    path('cards/', ListCard.as_view() , name='cards-list'),
    path('add-card/', CreateCard.as_view() , name='add-card'),

]

