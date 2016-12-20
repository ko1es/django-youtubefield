# -*- coding: utf-8 -*-
"""Model field."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from youtubeurl_field import formfields
from youtubeurl_field.validators import validate_youtube_url
from youtubeurl_field.youtubeurl import YoutubeUrl


class YoutubeUrlField(models.CharField):
    """Youtube field."""

    description = _("YouTube url")

    def __init__(self, *args, **kwargs):
        """Initial method."""
        super(YoutubeUrlField, self).__init__(*args, **kwargs)
        self.validators.append(validate_youtube_url)

    def get_internal_type(self):
        """Internal type method."""
        return "CharField"

    def to_python(self, value):
        """To python method."""
        if isinstance(value, YoutubeUrl):
            return value
        return YoutubeUrl(value)

    def get_prep_value(self, value):
        """Get prep value method."""
        value = super(YoutubeUrlField, self).get_prep_value(value)
        if isinstance(value, YoutubeUrl):
            return value.value
        return self.to_python(value)

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
