from django import forms
from .models import Category, Entry

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = {'text'}
        labels = {'text':''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'phone_number', 'name'}
        labels = {'name':'', 'phone_number':''}


