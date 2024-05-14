from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db import connection

@csrf_exempt
def login(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from akun")
        data = cursor.fetchall()
        print(data)
    return render(request, 'auth_login.html')