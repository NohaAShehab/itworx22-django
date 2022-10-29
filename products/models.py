from django.db import models
from django.shortcuts import  reverse, get_object_or_404

class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cat_name}"

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    @classmethod
    def get_object(cls, id):
        return get_object_or_404(cls, pk=id)

    def get_show_url(self):
        url = reverse("product.categories.show", args=[self.id])
        return url

# Create your models here.

# product ---> name, id , img , price , description, in_stock , no_of_items
class Product(models.Model):
    ## define the fields of the table
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="products/images/", null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    in_stock = models.BooleanField(default=False)
    no_of_items = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ### each product is under one category
    category = models.ForeignKey(Category,on_delete=models.CASCADE,
                                 null=True, related_name="category_products")

    def __str__(self):
        return self.name


    def get_show_url(self):
        url = reverse("products.show", args=[self.id])
        return url


    @classmethod
    def get_all_object(cls):
        return cls.objects.all()


    @classmethod
    def get_object(cls, id):
        return get_object_or_404(cls, pk=id)


    def get_image_url(self):
        return f"/media/{self.image}"


    def get_delete_url(self):
        delete_url = reverse("product.delete",args=[self.id])
        return delete_url

    def get_edit_url(self):
        edit_url = reverse("product.edit",args=[self.id])
        return edit_url

    @classmethod
    def delete_object(cls, id):
        deleted_object= cls.get_object(id)
        deleted_object.delete()
        return True


###########################
# student study many courses , courses studied by many students (many to many)
# student_name , course_name

### how ORM Works- --> Noha