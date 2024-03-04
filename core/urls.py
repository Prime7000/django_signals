

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail', views.detail, name='detail'),

    # Add other URL patterns for your app here if needed
]
