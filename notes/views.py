from django.shortcuts import render
from .models import notes
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

class NotesListVoew(ListView):
    model = notes # model that we're getting notes from
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NoteDetailView(DetailView):
    model = notes
    context_object_name = "note"


# class HomeView(TemplateView):

#     extra_context = 

# Create your views here.

# def list(request):
#     all_notes = notes.objects.all()
#     return render(request, "notes/notes_list.html", {'notes': all_notes})


# def detail(request, pk):
#     note = notes.objects.get(pk=pk)
#     return render(request, 'notes/notes_detail.html', {'note': note})