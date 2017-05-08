from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View, TemplateView

from .forms import ContactForm
from catalog.models import Category


def contact_form(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True

    return render(request, 'contact.html', {
        'form': form,
        'success': success
    })


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


def contact(request):
    return render(request, 'contact.html')
