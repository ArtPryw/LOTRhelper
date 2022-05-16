from django.urls import path

from . import views

urlpatterns = [
    path('heroes/', views.heroes, name='heroes'),
    path('', views.game, name='game'),
    path('detail/<int:character_id>/', views.detail, name='detail'),

]
