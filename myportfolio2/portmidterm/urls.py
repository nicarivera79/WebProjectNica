from django.urls import path
from portmidterm import views

urlpatterns = [
    path('portmidterm/', views.portmidterm, name='portmidterm'),
]