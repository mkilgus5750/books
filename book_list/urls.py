from django.urls import path
from . import views
urlpatterns = [
    path('', views.BookView.as_view()),
    path('submitted', views.SubmittedView.as_view()),
    path('books', views.BookList.as_view()),
    path('books/<int:pk>', views.BookDetail.as_view())
]