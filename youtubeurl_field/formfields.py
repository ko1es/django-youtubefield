from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _ 
from youtubeurl_field.validators import validate_youtube_url 
from youtubeurl_field.youtubeurl import to_python, YoutubeUrl 

class YoutubeUrlField(CharField):
    default_error_messages = {
        'invalid': _(u'Enter a valid url field.'),
    }
    default_validators = [validate_youtube_url]

    def to_python(self, value):
        youtube_url = to_python(value)
        if youtube_url and not youtube_url.is_valid():
            raise ValidationError(self.error_messages['invalid'])
        return youtube_url