from django.contrib import admin
from django.urls import path
from .views import CountriesList, CountriesDetail

urlpatterns = [
    path('countries/', CountriesList.as_view()),
    path('countries/<int:pk>/', CountriesDetail.as_view()),
]