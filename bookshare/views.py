from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serialziers import BookSerialzier, OrderSerializer, CitySerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .models import Book, Share, City, Category


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier
    permission_classes = [IsAuthenticated]


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzier
    permission_classes = [IsAuthenticated]


class ShareListCreateAPIView(ListCreateAPIView):
    queryset = Share.objects.all()
    serializer_class = OrderSerializer


class ShareRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Share.objects.all()
    serializer_class = OrderSerializer


class CityListCreateAPIView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CitySerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer