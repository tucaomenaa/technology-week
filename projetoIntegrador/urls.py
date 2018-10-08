from django.urls import path
from .views import *

urlpatterns = [
    path(r'', technology_week, name='technology_week'),
]