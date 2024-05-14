from django.urls import path
from authentikasi.views import *

app_name = 'auth'

urlpatterns = [
    path('login', login, name='login'),
]