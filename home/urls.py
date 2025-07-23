from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),                      # Homepage
    path('dashboard/', views.dashboard, name='dashboard'),   # Dashboard after login
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('destination/', views.destination, name='destination'),
    path('featured-destinations/', views.featured_destinations, name='featured_destinations'),
    path('get-a-quote/', views.get_a_quote, name='get_a_quote'),
    path('photo-story-1/', views.photo_story_1, name='photo_story_1'),
    path('photo-story-2/', views.photo_story_2, name='photo_story_2'),
    path('photo-story-3/', views.photo_story_3, name='photo_story_3'),
    path('pricing/', views.pricing, name='pricing'),
    path('sample-inner-page/', views.sample_inner_page, name='sample_inner_page'),
    path('service-details/', views.service_details, name='service_details'),
    path('travel-tips/', views.travel_tips, name='travel_tips'),
    path('video-gallery/', views.video_gallery, name='video_gallery'),

    # Auth routes
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('profile/', views.profile_view, name='profile'),  # Add this line
]
