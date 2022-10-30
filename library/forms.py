
from django import forms
from library.models import Book, Author
from betterforms.multiform import MultiModelForm

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields= '__all__'


##### Book , author at the same form
class AuthorModelForm(forms.ModelForm):
    class Meta:
        model= Author
        fields= '__all__'

class BookAuthorForm(MultiModelForm):
    form_classes = {
        'book':  BookModelForm ,
        'author': AuthorModelForm,
    }


    def save(self, commit=True):
        print("--------------save called ----------------------")
        objects = super(BookAuthorForm, self).save(commit=True)

        if commit:
            book = objects['book']
            book.save()
            author = objects['author']
            author.save()

        return objects

