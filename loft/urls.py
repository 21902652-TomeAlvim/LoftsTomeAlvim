from django.urls import path
from . import views

app_name = "loft"

urlpatterns = [
    path('', views.loft_home, name='home'),
    path('comment', views.comment_form, name="comment_form"),
    path('quizz', views.quizz_form, name="quizz_form")
]