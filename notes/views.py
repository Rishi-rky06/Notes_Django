import os
import time
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note

START_TIME = time.time()

def status_view(request):
    db_ok = True
    db_error = None
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchone()
    except Exception as e:
        db_ok = False
        db_error = str(e)

    uptime_seconds = int(time.time() - START_TIME)

    payload = {
        "ok": db_ok,
        "db_ok": db_ok,
        "db_error": db_error,
        "debug": settings.DEBUG,
        "version": getattr(settings, "APP_VERSION", "dev"),
        "commit": os.getenv("GIT_COMMIT", ""),
        "uptime_seconds": uptime_seconds,
    }
    return JsonResponse(payload, status=200 if db_ok else 503)

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, "notes/note_list.html", {"notes": notes})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect("notes:list")
    else:
        form = NoteForm()
    return render(request, "notes/note_form.html", {"form": form, "mode": "Create"})

@login_required
def note_edit(request, pk: int):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:list")
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form, "mode": "Edit"})

@login_required
def note_delete(request, pk: int):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("notes:list")
    return render(request, "notes/note_delete.html", {"note": note})
