from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):
    """
    Form for an entry in the diary
    """
    class Meta:
        model = Entry
        fields = ['author', 'title', 'text', 'created_date']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.instancia = kwargs.pop('instance', None)
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['author'].disabled = True
        self.initial['author'] = self.instancia
