from django.urls import path

from book_api.serializers import CustomAuthToken
from book_api.views import ShowAvailable, SignUp, Subscribe, NewBook, AllBooks, BookInformation, UpdateBookInformation, \
    DeleteBook, PersonalInformation, BookTitleSearch, BookSort

urlpatterns = [
    path('api/', ShowAvailable.as_view()),
    path('api/token/auth', CustomAuthToken.as_view()),
    path('api/signup', SignUp.as_view()),
    path('api/subscribe', Subscribe.as_view()),
    path('api/new', NewBook.as_view()),
    path('api/all', AllBooks.as_view()),
    path('api/<int:id>', BookInformation.as_view()),
    path('api/<int:id>/update', UpdateBookInformation.as_view()),
    path('api/<int:id>/delete', DeleteBook.as_view()),
    path('api/<str:username>', PersonalInformation.as_view()),
    path('api/search', BookTitleSearch.as_view()),
    path('api/sort', BookSort.as_view()),
]
