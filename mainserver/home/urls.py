from django.urls import path
from home.views import *

urlpatterns = [
    path('',detect_fake_news,name='Home'),
    path('about-us/',Content,name='Home'),
    path('<slug>/profile/',ProfileUpdate.as_view(),name='Home'),
    path('feedback/', feedback_view, name='feedback'),
    path('contact-us/', contact_view, name='feedback'),

]