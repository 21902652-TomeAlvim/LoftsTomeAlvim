from django.urls import path
from . import views

app_name = "loft"

urlpatterns = [
    path('', views.loft_home, name='home')
]