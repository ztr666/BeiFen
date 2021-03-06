from django.urls import path

from . import views

app_name = 'sightings'

urlpatterns = [
    path('', views.list_squirrels, name='list_squirrels'),
    path('<str:squirrel_id>/', views.edit_squirrels, name='edit_squirrels'),
    path('add/', views.add_squirrels, name='add_squirrels'),
    path('stats', views.stats, name='stats'),
    path('<str:squirrel_id>/detail/', views.detail, name='detail'),
]
