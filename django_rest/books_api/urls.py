from django.urls import path

from django_rest.books_api.views import BookListCreate, BookGetUpdateDelete

urlpatterns = [
    path('', BookListCreate.as_view()),
    path('<int:book_id>', BookGetUpdateDelete.as_view()),
]