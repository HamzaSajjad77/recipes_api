from django.urls import path
from . import views

urlpatterns = [
   path('recipe/', views.recipes_list, name='recipe-list-create'),
   path('recipe/create', views.recipe_list_create, name='recipe-list-create'),
   path('recipe/<int:pk>', views.recipe_details, name='recipe-details')
]