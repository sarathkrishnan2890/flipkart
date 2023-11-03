from django.urls import path
from . views import SignupPage

urlpatterns=[
    path('signup/',SignupPage.as_view(),name='signup')
]