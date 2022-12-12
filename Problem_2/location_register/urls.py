from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.location_form, name='location_insert'),  # get and post req. for insert operation
    path('<int:id>/', views.location_form, name='location_update'),  # get and post req. for update operation
    path('delete/<int:id>/', views.location_delete, name='location_delete'),
    path('list/', views.location_list, name='location_list'),  # get req. to retrieve and display all records
]
