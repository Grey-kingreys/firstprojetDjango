from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    # Ajoutez d'autres URLs de blog ici au besoin
]
