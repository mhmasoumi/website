from django.db import models
from django.urls import reverse
#from django.core.urlresolverse import reverse     -> in the tutorial

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    genre = models.CharField(max_length=150)
    album_logo = models.FileField()


    # get_absolute_url is a special function
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})   #just redirecting it

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=300)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
