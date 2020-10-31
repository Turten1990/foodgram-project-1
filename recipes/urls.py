from django.urls import include, path
from . import views 

urlpatterns = [
    path('', views.index, name = "index"), 
    path('new/', views.new, name='new'),
    path('ingredients', views.ingredients, name='ingredients')
]