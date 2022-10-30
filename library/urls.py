from django.urls import path, include
from library.views import CreateBookView,Book_Create_Generic_View, \
    Edit_Book_Generic_View, Book_List_View, Book_Detail_View, \
    Delete_Book_View, BookAuhtorView

urlpatterns = [
    path("book/create", CreateBookView.as_view(), name="createbookview"),
    path("book/generic/create",Book_Create_Generic_View.as_view(), name="createbook" ),
    path("book/edit/<int:pk>", Edit_Book_Generic_View.as_view(), name="editbook"),
    path("book/index", Book_List_View.as_view(), name="book.index"),
    path("book/<int:pk>", Book_Detail_View.as_view(), name='book.show'),
    path("book/delete/<int:pk>", Delete_Book_View.as_view(), name="book.delete"),
    path("bookauthor",BookAuhtorView.as_view(),name="book_author" )

]