from django.urls import path

from drinks import views

urlpatterns = [
    path('drinks/', views.drinks_list),
    path('drinks/<int:id>', views.drink_detail)
]