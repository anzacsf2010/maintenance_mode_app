from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('maintenance', views.maintenance, name='maintenance'),
]