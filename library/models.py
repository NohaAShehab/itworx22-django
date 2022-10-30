from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, null=True)
    image = models.ImageField(upload_to="library/authors/images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def save_author(cls, name, email,image):
        author = cls.objects.create(name=name, email=email, image=image)
        return author


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="library/books/images/", null=True, blank=True)
    no_of_pages = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_edit_url(self):
        url = reverse("editbook", args=[self.id])
        return url

    def get_show_url(self):
        url = reverse("book.show", args=[self.id])
        return url

    def get_image_url(self):
        return f"/media/{self.image}"

    def get_delete_url(self):
        url = reverse("book.delete", args=[self.id])
        return url

    @classmethod
    def savemybook(cls, name, description, image, no_of_pages, author):

        book = cls.objects.create(name=name, description=description,
            image=image, no_of_pages=no_of_pages, author=author)
        return book