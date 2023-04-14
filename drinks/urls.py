from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from drinks import views

urlpatterns = [
    path('drinks/', views.drinks_list),
    path('drinks/<int:id>', views.drink_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
