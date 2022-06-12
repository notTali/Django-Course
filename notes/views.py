from django.shortcuts import render
from .models import notes

# Create your views here.

def list(request):
    all_notes = notes.objects.all()
    return render(request, "notes/notes_list.html", {'notes': all_notes})


def detail(request, pk):
    note = notes.object.get(pk=pk)
    return render(request, 'notes/notes_detail.html', {'note', note})