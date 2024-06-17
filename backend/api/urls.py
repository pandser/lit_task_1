from django.urls import path

from api.views import TestView


urlpatterns = [
    path('test/', TestView.as_view()), 
]
