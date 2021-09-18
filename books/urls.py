from django.urls import path
from .views import BookListView, BookDetailView
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    # with primary key
    # path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail')
]