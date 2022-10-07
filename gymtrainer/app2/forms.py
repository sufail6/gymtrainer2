from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import DateInput

from app2 import models
from app2.models import Login, Equipments, Bill


class TrainerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2','name','age','email','address','contact_no','photo')


class UserForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2','name','age','email','address','contact_no')


class Product(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = '__all__'


class AddBill(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ('status', 'paid_on')

