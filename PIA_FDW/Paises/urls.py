from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('china/', views.china, name='china'),
    path('arabe/', views.arabe, name='arabe'),
    path('corea/', views.corea, name='corea'),
    path('japon/', views.japon, name='japon'),
    path('hungria/', views.hungria, name='hungria'),
    path('encuesta/', views.encuesta_view, name='encuesta'),
    path('gracias/', views.gracias_view, name='gracias'),
]