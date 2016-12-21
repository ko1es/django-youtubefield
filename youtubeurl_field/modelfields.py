# -*- coding: utf-8 -*-
"""Model field."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from youtubeurl_field import formfields
from youtubeurl_field.validators import validate_youtube_url
from youtubeurl_field.youtubeurl import YoutubeUrl


class YoutubeUrlField(models.URLField):
    """Youtube field."""

    description = _("YouTubeUrl")

    def __init__(self, *args, **kwargs):
        """Initial method."""
        super(YoutubeUrlField, self).__init__(*args, **kwargs)
        self.validators.append(validate_youtube_url)

    def to_python(self, value):
        """To python method."""
        return YoutubeUrl(value)

    def formfield(self, **kwargs):
        """Form field method."""
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
