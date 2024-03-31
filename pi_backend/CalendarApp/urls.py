from django.urls import path
from .views import *

urlpatterns = [
    path('event/', CalendarView.as_view(), name='event'),
]