from django.contrib import admin
from django.urls import path
from .views import CategoryList,CategoryDetails,BookList,BookDetails,ProductList,ProductDetails

urlpatterns = [
    path('categories/' , CategoryList.as_view()),
    path('category/<int:pk>/' , CategoryDetails.as_view()),
    path('books/' , BookList.as_view()),
    path('book/<int:pk>/', BookDetails.as_view()),
    path('products/',ProductList.as_view() ),
    path('product/<int:pk>/', ProductDetails.as_view()),
]