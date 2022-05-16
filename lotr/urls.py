from django.urls import path

from . import views

urlpatterns = [
    path('', views.heroes, name='heroes'),
    path('', views.game, name='game'),
    path('<int:character_id>/', views.detail, name='detail'),

]
