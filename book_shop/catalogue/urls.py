from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='main'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('catalogue/<int:catalogue_id>/', view_catalogue, name='view_catalogue'),
    path('catalogue/add_book/', add_book, name='add_book'),
]