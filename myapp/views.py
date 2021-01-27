import csv
import datetime

# import xlwt
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm, SnippetForm
from .models import Snippet

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            print(fname, lname, email)

    form = ContactForm()
    return render(request, 'form.html', {'form': form})


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            print('VALIDDDDD')

    form = SnippetForm()
    return render(request, 'form.html', {'form': form})


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename = Data " + \
        str(datetime.datetime.now())+".csv"

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Body'])
    snippets = Snippet.objects.all()
    for snip in snippets:
        writer.writerow([snip.fname, snip.lname,
                         snip.email, snip.body])

    return response
