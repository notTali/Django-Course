from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NotesListVoew.as_view()),
    path('notes/<int:pk>', views.NoteDetailView.as_view()), #receives an int value as a primary key
]