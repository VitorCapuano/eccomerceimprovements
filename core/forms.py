from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome: {}\nEmail: {}\n{}'.format(name, email, message)
        send_mail(
            'Contato Ecom', message, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )
