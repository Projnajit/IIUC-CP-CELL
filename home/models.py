from django.db import models
from embed_video.fields import EmbedVideoField

mytuple =(
    ("Algorithm", "Algorithm"),
    ("Data Structures", "Data Structures"),
    ("Dynamic Programming", "Dynamic Programming"),
    ("Mathematics", "Mathematics"),
    ("Implementation", "Implementation"),
    ("String", "String"),
    ("Searching and Sortings", "Searching and Sortings"),
    ("Graph", "Graph"),
    ("Geometry", "Geometry"),
    ("Miscellaneous", "Miscellaneous"),
    ("Live Contests", "Live Contests"),

)

class Video(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255,choices=mytuple,default="Live Contest")
    added = models.DateTimeField(auto_now_add=True)
    ps = models.IntegerField(default=0)
    url = EmbedVideoField()
    uploader = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-added']