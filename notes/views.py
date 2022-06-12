from django.shortcuts import render
from .models import notes

# Create your views here.

def list(request):
    all_notes = notes.objects.all()
    return render(request, "notes_list.html", {'notes': all_notes})