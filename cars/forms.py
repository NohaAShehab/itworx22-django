
from django import forms

from cars.models import Brand, Car

class CarForm(forms.Form):
    name = forms.CharField(max_length=100, label="Car name ")
    email= forms.EmailField()
    image = forms.ImageField()
    price = forms.IntegerField()
    in_stock = forms.BooleanField()
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())



class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        #validation rules