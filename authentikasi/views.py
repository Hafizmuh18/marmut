from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

@csrf_exempt
def login(request):
    return render(request, 'auth_login.html')