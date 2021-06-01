from django.contrib import admin
from django.urls import path, include

from catalog import views

urlpatterns = [
    path('catalog_list/', views.AuthorListView.as_view(), name='catalog_list')
]
