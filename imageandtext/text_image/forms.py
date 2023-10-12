# forms.py in your app
from django import forms
from .models import hadithsModel, tatorial


class hadithsForm(forms.ModelForm):
    class Meta:
        model = hadithsModel
        fields = ['chapter_name','hadith_number', 'text', 'hadith_status']
        labels = {'chapter_name':'Chapter Name','hadith_number': 'Hadith Number', 'text': 'Hadith Text', 'hadith_status': 'Hadith Status'}
        widgets = {
            'hadith_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'hadith_status': forms.Select(attrs={'class': 'form-control'}),
            'chapter_name': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class tatorialForm(forms.ModelForm):
    class Meta:
        model = tatorial
        fields = ['title', 'description', 'image']
        labels = {'title': 'Title', 'description': 'Description', 'image': 'Image'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
        



