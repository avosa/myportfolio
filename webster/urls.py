from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('', views.index, name='home'), #home
    path('project', views.project, name='project'), #project
    path('contact', views.contact, name='contact'), #contact
    path('about', views.about, name='about'), #about
]