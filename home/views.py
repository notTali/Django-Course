from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home/welcome.html', {"today": datetime.today()}) #brackets for passing value to the view

@login_required(login_url='/admin') #restrict this page to logged in users only.
def authorized(request):
    return render(request, 'home/authorized.html', {})