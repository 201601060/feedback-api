from django.db import models
from django.db.models.fields.json import JSONField

# Create your models here.


class Submission(models.Model):
    data = JSONField(null=True, blank=True)
    comment = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.id

    def save(self, *args, **kwargs):
        super(Submission, self).save(*args, **kwargs)
