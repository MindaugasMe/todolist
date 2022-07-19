from django.urls import path
from . import views 


urlpatterns = [
    path('calculator/', views.index, name='index'),
    path('calculator/count', views.count, name='count'),
    ]