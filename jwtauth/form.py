from django import forms
from jwtauth.models import EmailPush

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailPush
        exclude = ['email_send', 'user']
        widgets = {
            'Push_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }