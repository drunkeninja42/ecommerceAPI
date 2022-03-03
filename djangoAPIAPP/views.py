from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,BookSerializer,ProductSerializer
from .models import Category,Book,Product
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class CategoryList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self , request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetails(APIView):
    def get_object(self ,pk):
        try:
            return Category.objects.get(pk = pk)
        except Category.DoesNotExist:
            raise Http404
    def get(self , request):
        category = self.get_object(pk)
        serializer = CategorySerializer(category , many = True)
        return Response(serializer.data)
    def put(self , request):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self , request):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookList(APIView):

    def get(self , request):
        books = Book.objects.all()
        serializer = BookSerializer(books , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def get_object(self ,pk):
        try:
            return Book.objects.get(pk = pk)
        except Book.DoesNotExist:
            raise Http404
    def get(self , request):
        book = self.get_object(pk)
        serializer = BookSerializer(book , many = True)
        return Response(serializer.data)
    def put(self , request):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self , request):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
    def get(self , request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):
    def get_object(self ,pk):
        try:
            return Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            raise Http404
    def get(self , request):
        product = self.get_object(pk)
        serializer = ProductSerializer(product , many = True)
        return Response(serializer.data)
    def put(self , request):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self , request):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

