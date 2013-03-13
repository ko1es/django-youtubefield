import urlparse
from django.db import models
from django import  forms
from django.utils.translation import ugettext_lazy as _ 
from youtubeurl_field import formfields
from youtubeurl_field.validators import validate_youtube_url
from youtubeurl_field.youtubeurl import to_python, YoutubeUrl 
 
class YoutubeUrlField(models.URLField):
    __metaclass__ = models.SubfieldBase
    description = _("YouTube url")
 
    def __init__(self, *args, **kwargs):
        super(YoutubeUrlField, self).__init__(*args, **kwargs)
        self.validators.append(validate_youtube_url)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': formfields.YoutubeUrlField,
        }
        defaults.update(kwargs)
        return super(YoutubeUrlField, self).formfield(**defaults)
    
    def to_python(self, value):
        url = super(YoutubeUrlField, self).to_python(value)
        return YoutubeUrl(url)

    def get_prep_value(self, value):
        return unicode(value)
 
 
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