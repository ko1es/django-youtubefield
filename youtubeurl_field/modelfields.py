import urlparse
from django.db import models
from django import  forms
from django.utils.translation import ugettext_lazy as _ 
from django.utils import six

from youtubeurl_field import formfields
from youtubeurl_field.validators import validate_youtube_url
from youtubeurl_field.youtubeurl import YoutubeUrl
 
class YoutubeUrlField(models.CharField):
    __metaclass__ = models.SubfieldBase
    description = _("YouTube url")
    
    def __init__(self, *args, **kwargs):
        super(YoutubeUrlField, self).__init__(*args, **kwargs)
        self.validators = (validate_youtube_url,)

    def get_internal_type(self):
        return "CharField"
    
    def to_python(self, value):
        if isinstance(value, YoutubeUrl):
            return value
        return YoutubeUrl(value)

    def get_prep_value(self, value):
        return self.to_python(value)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': formfields.YoutubeUrlField,
        }
        defaults.update(kwargs)
        return super(YoutubeUrlField, self).formfield(**defaults)

 
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([
        (
            [YoutubeUrlField],
            [],
            {},
        ),
    ], ["^youtubeurl_field\.modelfields\.YoutubeUrlField"])
except ImportError:
    pass
