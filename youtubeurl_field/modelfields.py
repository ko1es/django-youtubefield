import urlparse
from django.db import models
from django import  forms
from django.utils.translation import ugettext_lazy as _ 
from youtubeurl_field import formfields
from youtubeurl_field.validators import validate_youtube_url

 
class YoutubeUrl(unicode):
    @property
    def video_id(self):
        parsed_url = urlparse.urlparse(self)
        if parsed_url.query == '':
            return parsed_url.path
        return urlparse.parse_qs(parsed_url.query)['v'][0]
 
    @property
    def embed_url(self):
        return 'http://youtube.com/embed/%s/' % self.video_id
 
    @property
    def thumb(self):
        return "http://img.youtube.com/vi/%s/2.jpg" % self.video_id
 
 
class YoutubeUrlField(models.URLField):
    __metaclass__ = models.SubfieldBase
    description = _("YouTube url")
 
    def __init__(self, *args, **kwargs):
        super(YoutubeUrlField, self).__init__(*args, **kwargs)
        self.validators.append(validate_youtube_url)
 
    def to_python(self, value):
        url = super(YoutubeUrlField, self).to_python(value)
        return YoutubeUrl(url)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': formfields.YoutubeUrlField,
        }
        defaults.update(kwargs)
        return super(YoutubeUrlField, self).formfield(**defaults)
 
    def get_prep_value(self, value):
        return unicode(value)
 
 
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([],  ["^fields\.YoutubeUrlField"])
except ImportError:
    pass