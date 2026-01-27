from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            "body": forms.Textarea(attrs={"rows": 8, "placeholder": "Write something..."}),
        }
