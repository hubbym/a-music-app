from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length = 100 ,)
    album_title = models.CharField(max_length = 500 ,)
    genre= models.CharField(max_length = 100 , )
    album_logo = models.ImageField(null = True , blank = True)

    def __str__ (self):
        return self.album_title + 'by' + self.artist

    @property
    def imageURL(self):
        try:
            url = self.album_logo.url
        except:
            url = ""
        return url     

class Song(models.Model):
      album = models.ForeignKey(Album, on_delete = models.CASCADE) 
      file_type = models.CharField(max_length = 19)
      song_title = models.CharField(max_length = 100)
      is_favorite = models.BooleanField(default = False)
      def __str__ (self) :
          return  self.song_title