from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from learning.forms import RegistrationForm
from .models import Course, Student, Teacher, Category


def home_view(request):
    context = {
        'objects': Course.objects.all()
    }
    return render(request, 'learning/home.html', context=context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form, type(form))
            # email = form.objects.get('email')
            # raw_password = form.objects.get('password')
            account = authenticate(email=email, password=password1)
            login(request, account)
            return redirect('home')
        else:
            context["registration_form"] = form
    else:  # get request
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, 'learning/register.html', context=context)
