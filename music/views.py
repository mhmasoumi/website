from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album



class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class CreateAlbum(CreateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo'] #uses form_album form.html as default

class UpdateAlbum(UpdateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']  #uses form album_form.html as default

class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
