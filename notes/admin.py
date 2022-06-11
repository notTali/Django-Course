from django.contrib import admin
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


# Register your models here.
admin.site.register(models.notes, NotesAdmin)