from django.urls import path
from newforms.views import home
urlpatterns = [
    path('',home),
]