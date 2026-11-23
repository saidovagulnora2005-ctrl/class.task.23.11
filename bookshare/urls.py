from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, CityListCreateAPIView, CityRetrieveUpdateDestroyAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, ShareListCreateAPIView, ShareRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('book/', BookListCreateAPIView.as_view()),
    path('book/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('city/', CityListCreateAPIView.as_view()),
    path('city/<int:pk>/', CityRetrieveUpdateDestroyAPIView.as_view()),
    path('share/', ShareListCreateAPIView.as_view()),
    path('share/<int:pk>/', ShareRetrieveUpdateDestroyAPIView.as_view()),
]