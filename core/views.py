import math

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from items.models import Item, Category
from django.contrib import messages
from .models import Cities, CustomUser
from .forms import SignupForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from .forms import ContactForm


# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False).order_by("-created_at")
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            fullname = form.cleaned_data['fullname']
            phonenumber = form.cleaned_data['phonenumber']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose email
            subject = 'Contact Form Submission'
            body = f"Full Name: {fullname}\nPhone Number: {phonenumber}\nEmail: {email}\n\nMessage:\n{message}"

            # Send email
            email_message = EmailMessage(subject, body, to=['princeartasmenetil@gmail.com'])
            email_message.send()

            # Redirect after successful submission
            return HttpResponseRedirect('/contact/')  # Redirect to a success page

    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def privacy_and_policy(request):
    return render(request, 'core/privacy_and_policy.html')

def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')

def about(request):
    return render(request, 'core/about.html')

def get_cities(request):
    region_id = request.GET.get('region_id')
    cities = Cities.objects.filter(region_id=region_id).order_by('name')
    data = [{'id': city.id, 'name': city.name} for city in cities]
    return JsonResponse(data, safe=False)


def login(request):
    forms = SignupForm(request.POST)
    return render(request, 'core:login', {
        'forms': forms,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.region = form.cleaned_data.get('region')
            user.city = form.cleaned_data.get('city')
            user.save()
            logout(request)
            return redirect('core:login')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def profile(request, user):
    user = request.user
    return render(request, 'core/profile.html', {'user': user})

@login_required
def profile_edit(request, user):
    user = get_object_or_404(CustomUser, username=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('core:profile', user=user.username)
    else:
        form = ProfileEditForm(instance=user)
    return render(request, 'core/profile_edit.html', {
        'form': form,
        'title': 'Edit Profile',
        'user': user,
    })
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('/')
    return render(request, '/')


@login_required
def dashboard(request, user):
    items = Item.objects.filter(created_by=request.user).order_by('-created_at')
    user = request.user
    return render(request, "core/dashboard.html", {
        'items': items,
        'user': user,
    })
