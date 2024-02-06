from django.urls import path
from . import views
from .views import (
    CreatePage, 
    ListPage,
    EditPage,
    DeletePage,
    HomeList,
    HomeCreate,
    HomeEdit,
    CreateAppointment,
    ListAppointment,
    EditAppointment,
    DeleteAppointment,
)
urlpatterns = [
    # pages CRUD
    path('', views.AdminHome, name='AdminHome'),
    path('add-page/', CreatePage.as_view() , name='add-page'),
    path('pages/', ListPage.as_view() , name='pages-list'),
    path('edit-page/<int:pk>/', EditPage.as_view() , name='edit-page'),
    path('delete-page/<int:pk>/', DeletePage.as_view() , name='delete-page'),
    
    #HomePgeContent CRUD
    path('list/', HomeList.as_view() , name='list'),
    path('add/', HomeCreate.as_view() , name='add'),
    path('edit/<int:pk>/', HomeEdit.as_view() , name='edit'),
    
    #Appointment CRUD
    path('appointment/', ListAppointment.as_view() , name='appointment-list'),
    path('add-appointment/', CreateAppointment.as_view() , name='add-appointment'),
    path('edit-appointment/<int:pk>/', EditAppointment.as_view() , name='edit-appointment'),
    path('delete-appointment/<int:pk>/', DeleteAppointment.as_view() , name='delete-appointment'),

]

