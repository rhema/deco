from django.db import models
from django.template.loader import render_to_string
#http://stackoverflow.com/questions/929029/how-do-i-access-the-child-classes-of-an-object-in-django-without-knowing-the-nam/929982#929982

from django.contrib.contenttypes.models import ContentType

class InheritanceCastModel(models.Model):
    """
    An abstract base class that provides a ``real_type`` FK to ContentType.

    For use in trees of inherited models, to be able to downcast
    parent instances to their child types.

    """
    real_type = models.ForeignKey(ContentType, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(InheritanceCastModel, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def cast(self):
        return self.real_type.get_object_for_this_type(pk=self.pk)

    class Meta:
        abstract = True


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    snippet = models.TextField()
    
    def __unicode__(self):
        return self.tag

class Item(InheritanceCastModel):
    title = models.CharField(max_length = 200)
    tags = models.ManyToManyField(Tag, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
#    topImage = models.ImageField(upload_to='images')
    def __unicode__(self):
        return self.title

    def url(self):
        stripped = self.title.replace(' ','_')
        return stripped
    
    def render(self):
        print "<h1>"+self.title+"</h1>"
        return "<h1>"+self.title+"</h1>"

class Post(Item):
    body = models.TextField()
    def render(self):
        print render_to_string('post.html',{'title': self.title, 'body': self.body })
        return render_to_string('post.html',{'title': self.title, 'body': self.body })