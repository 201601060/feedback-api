import json
import logging

from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django_json_widget.widgets import JSONEditorWidget

from submissions.models import Submission

# Register your models here.

logger = logging.getLogger(__name__)


# class PrettyJSONWidget(widgets.Textarea):
#
#     def format_value(self, value):
#         try:
#             value = json.dumps(json.loads(value), indent=2, sort_keys=True)
#             # these lines will try to adjust size of TextArea to fit to content
#             row_lengths = [len(r) for r in value.split('\n')]
#             self.attrs['rows'] = min(max(len(row_lengths) + 2, 10), 30)
#             self.attrs['cols'] = min(max(max(row_lengths) + 2, 40), 120)
#             return value
#         except Exception as e:
#             logger.warning("Error while formatting JSON: {}".format(e))
#             return super(PrettyJSONWidget, self).format_value(value)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
        models.CharField: {'widget': Textarea}
    }
    pass


admin.site.register(Submission, SubmissionAdmin)
