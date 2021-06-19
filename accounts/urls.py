
from django.urls import path
from .views import *
urlpatterns = [
    path('', view=Home ),
    path('register', RegisterView.as_view())
]
