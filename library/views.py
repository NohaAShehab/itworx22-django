from django.shortcuts import render, redirect

# Create your views here.

from django import  views
from library.forms import  BookModelForm, BookAuthorForm
from django.http import  HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from library.models import Book, Author
from django.views.generic import  CreateView as CreateCustomView

# ## pure class based views
class CreateBookView(views.View):
    ### implement 2 function
    def get(self, request):
        form = BookModelForm()
        return render(request, "library/create.html", context={"form":form})

    def post(self, request):
        form = BookModelForm(request.POST, request.FILES)
        form.save()
        return HttpResponse("new book added ")

#######################################
### generic views

##### create class for each Action

#### create
class Book_Create_Generic_View(CreateView):
    form_class = BookModelForm
    template_name = "library/create.html"
    success_url = "/library/book/index"



class Edit_Book_Generic_View(UpdateView):
    form_class = BookModelForm
    template_name = "library/edit.html"
    model = Book
    success_url = "/library/book/index"



### view one object



### delete object



### list all items
##3 get all items from the models

class Book_List_View(ListView):
    model = Book
    template_name = "library/index.html"
    context_object_name = "books"


class Book_Detail_View(DetailView):
    model = Book
    template_name = "library/show.html"
    # context_object_name = "book"



class Delete_Book_View(DeleteView):
    model = Book
    template_name = "library/delete.html"
    success_url = "/library/book/index"



class BookAuhtorView(CreateCustomView):
    form_class = BookAuthorForm
    success_url = "/"
    template_name = "library/createauthorbook.html"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        author = Author.save_author(request.POST["author-name"], request.POST["author-email"], request.FILES['author-image'])
        print(author)

        book = Book.savemybook(request.POST["book-name"],
            request.POST["book-description"], request.FILES["book-image"],
                           request.POST["book-no_of_pages"], author)
        return HttpResponse("Hi")




    # def form_valid(self, form):
    #     author = form['auhtor'].save()
    #     print(f"---------------- {author}")
    #     book = form["book"].save()
    #     return redirect("/")

