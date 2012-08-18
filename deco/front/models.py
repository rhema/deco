from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
#    topImage = models.ImageField(upload_to='images')
    def __unicode__(self):
        return self.title

    def url(self):
        stripped = self.title.replace(' ','_')
        return stripped