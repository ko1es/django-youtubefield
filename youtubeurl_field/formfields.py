# -*- coding: utf-8 -*-
"""Form fields."""
from django.forms.fields import CharField
from django.utils.translation import ugettext_lazy as _
from youtubeurl_field.validators import validate_youtube_url
from youtubeurl_field.youtubeurl import YoutubeUrl


class YoutubeUrlField(CharField):
    """Youtube form field."""

    default_error_messages = {
        'invalid': _('Enter a valid URL.'),
    }

    def __init__(self, **kwargs):
        """Initial method."""
        super(YoutubeUrlField, self).__init__(**kwargs)
        self.validators = [validate_youtube_url, ]

    def to_python(self, value):
        """To python method."""
        return YoutubeUrl(value)
