from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('new/', views.new, name='new'),
    path('<str:slug>/', views.detail, name='detail'),
]
