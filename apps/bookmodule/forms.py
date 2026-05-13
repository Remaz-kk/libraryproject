from django import forms
from .models import Book
from django import forms
from .models import Student, Address, Student2, Address2, StudentImage


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = '__all__'


class Student2Form(forms.ModelForm):

    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']

        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }


class StudentImageForm(forms.ModelForm):
    class Meta:
        model = StudentImage
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'publisher', 'authors']



