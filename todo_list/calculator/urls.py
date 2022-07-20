from django.urls import path
from . import views 


urlpatterns = [
    path('calculator/', views.index, name='index'),
    path('calculator/count', views.count_calories, name='count'),
    path('calculator/history', views.history, name='history'),
    ]