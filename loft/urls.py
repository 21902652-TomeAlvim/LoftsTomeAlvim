from django.urls import path
from . import views

app_name = "loft"

urlpatterns = [
    path('', views.loft_home, name='home'),
    path('comment', views.comment_form, name="comment_form"),
    path('quizz', views.quizz_form, name="quizz_form"),
    path('loft/<int:loft_id>', views.loft_page, name="loft_page"),
    path('contact/<int:loft_id>', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('profile', views.profile, name="profile"),
    path('logout', views.logout, name="logout"),
    path('quizz_result/<int:quizz_id>', views.quizz_result, name="quizz_result"),
    path('delete_loft/<int:loft_id>', views.delete_loft, name="delete_loft"),
    path('delete_contact/<int:contact_id>', views.delete_contact, name="delete_contact"),
]