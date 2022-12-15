from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4

class Website(models.Model):
    storybookName = models.CharField(null=True, blank=True, max_length=200)
    storybookStory = models.TextField(null=True, blank=True)
    coverImage = models.ImageField(default='default.jpeg', upload_to='cover_page_images')

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.storybookName, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.slug = slugify('{} {}'.format(self.storybookName, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Website, self).save(*args, **kwargs)
