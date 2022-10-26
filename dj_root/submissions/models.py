from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Submission(models.Model):
    name = models.CharField(max_length=255)
    data = JSONField(null=True, blank=True)
    comment = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Submission, self).save(*args, **kwargs)
