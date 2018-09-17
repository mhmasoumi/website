from django.urls import path, re_path
from . import views

#namespacing for urls just with this syntax
app_name = 'music'


# viwes.index() is just a function that gets a request and response like :       index(req) -> res
# views.detail() is a function with a diffrent format like:        detail(req, album_id) -> res      album_id is the captured group
urlpatterns = [
    #/music/   -> exctly matches only this
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    #/music/<album_id>  -> the number is the album id
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #music/album/add
    re_path(r'album/add/$', views.CreateAlbum.as_view(), name='add-album'),

    #music/album/<album.id>
    re_path(r'album/(?P<pk>[0-9]+)$', views.UpdateAlbum.as_view(), name='update-album'),

    #music/album/<album.id>/delete
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='delete-album'),

]
