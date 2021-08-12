from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Введите ваш телефон'}))

    class Meta:
        model = Feedback
        fields = ['name', 'phone']