from django.shortcuts import render, redirect, HttpResponse
from home.models import Contact
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.travel_predictor import TravelPredictor
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.travel_predictor import TravelPredictor

# Load predictor once
predictor = TravelPredictor()
predictor.load_data()

@login_required
def dashboard(request):
    errors = []
    prediction = None

    if request.method == "POST":
        user_input = {
            'destination_type': request.POST.get('destination_type', '').strip(),
            'preferred_climate': request.POST.get('preferred_climate', '').strip(),
            'distance': request.POST.get('distance', '').strip(),
            'budget': request.POST.get('budget', '').strip(),
            'food_preference': request.POST.get('food_preference', '').strip(),
            'activity_preference': request.POST.get('activity_preference', '').strip(),
        }

        # Validate all required fields
        missing = [k for k, v in user_input.items() if not v]
        if missing:
            errors.append(f"Please fill all fields: {', '.join(missing)}")

        if not errors:
            try:
                prediction = predictor.predict_destination(user_input)
            except Exception as e:
                errors.append(f"Prediction error: {str(e)}")

    return render(request, 'dashboard.html', {'errors': errors, 'prediction': prediction})


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Your message has been successfully sent!")

    return render(request, 'contact.html')


def destination(request):
    return render(request,'destination.html')

def featured_destinations(request):
    return render(request,'featured-destinations.html')

def get_a_quote(request):
    return render(request,'get-a-quote.html')

def photo_story_1(request):
    return render(request,'photo-story-1.html')

def photo_story_2(request):
    return render(request,'photo-story-2.html')

def photo_story_3(request):
    return render(request,'photo-story-3.html')

def pricing(request):
    return render(request,'pricing.html')

def sample_inner_page(request):
    return render(request,'sample-inner-page.html')

def service_details(request):
    return render(request,'service-details.html')

def travel_tips(request):
    return render(request,'travel-tips.html')

def video_gallery(request):
    return render(request,'video-gallery.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Registration successful. You are now logged in.")
                    return redirect('dashboard')
                else:
                    messages.error(request, "Authentication failed after registration.")
            except Exception as e:
                messages.error(request, "User already exists or some error occurred.")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'profile.html')
    