from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import Entry
from .forms import EntryForm
from gym.views import UserProfile

# Create your views here.


def entry_list(request):
    """
    Show all entries of the diary
    """
    try:
        entries = Entry.objects.filter(author__user=request.user)
    except Entry.DoesNotExist:
        entries = ''
    return render(request, 'diario/entry_list.html', {'entries': entries})


class EntryDetailView(generic.DetailView):
    """
    Generic view for the entry detail
    """
    model = Entry


class EntryUpdateView(SuccessMessageMixin, generic.UpdateView):
    """
    Generic view for update an entry
    """
    model = Entry
    fields = ['title', 'text', 'created_date']
    template_name_suffix = '_update_form'
    success_message = 'Entrada actualizada correctamente'

    def get_success_url(self):
        return reverse('entry_list')


def post_entry(request):
    """
    View for a new entry in the diary
    """
    if request.method == "POST":
        form = EntryForm(request.POST, request=request)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = UserProfile.objects.get(user=request.user)
            try:
                profile.save()
                messages.success(
                    request, 'Entrada añadida correctamente')
            except Exception as e:
                messages.error(
                    request, 'Ocurrió un error al añadir la entrada')
            return redirect('entry_list')
    else:
        if not request.user.is_anonymous:
            user_entry = UserProfile.objects.get(user=request.user)
            form = EntryForm(request=request, instance=user_entry)
        else:
            form = EntryForm()

    return render(request, 'diario/post_entry.html', {'form': form})


class EntryDelete(generic.DeleteView):
    """
    Generic view to delete an entry
    """
    model = Entry
    context_object_name = 'entry'
    success_message = 'Entrada eliminada correctamente'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(EntryDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('entry_list')
