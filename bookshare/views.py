from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serialziers import BookSerialzier
from rest_framework.permissions import IsAuthenticated


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerialzier
    permission_classes = [IsAuthenticated]


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerialzier
    permission_classes = [IsAuthenticated]