from django.urls import path
from . import views
from .views import (
    CreatePage, 
    ListPage,
    EditPage,
    DeletePage,
    # ListCard, 
    # CreateCard,
    # EditCard,
    HomeList,
    HomeCreate,
    HomeEdit
)
urlpatterns = [
    # pages CRUD
    path('', views.AdminHome, name='AdminHome'),
    path('add-page/', CreatePage.as_view() , name='add-page'),
    path('pages/', ListPage.as_view() , name='pages-list'),
    path('edit-page/<int:pk>/', EditPage.as_view() , name='edit-page'),
    path('delete-page/<int:pk>/', DeletePage.as_view() , name='delete-page'),
    #Top Cards CRUD
    # path('cards/', ListCard.as_view() , name='cards-list'),
    # path('add-card/', CreateCard.as_view() , name='add-card'),
    # path('edit-card/<int:pk>/', EditCard.as_view() , name='edit-card'),
    #HomePgeContent CRUD
    path('list/', HomeList.as_view() , name='list'),
    path('add/', HomeCreate.as_view() , name='add'),
    path('edit/<int:pk>/', HomeEdit.as_view() , name='edit'),

]

