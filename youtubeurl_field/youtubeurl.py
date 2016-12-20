# -*- coding: utf-8 -*-
"""YoutubeUrl obejct."""
import urlparse
import os
from django.core.validators import EMPTY_VALUES


class YoutubeUrl(object):
    """Base class."""

    def __init__(self, value):
        """Initial method."""
        self.value = value

    def is_empty(self):
        """Empty checking."""
        return True if self.value in EMPTY_VALUES else False

    @property
    def video_id(self):
        """Video id property."""
        if not self.is_empty():
            parsed_url = urlparse.urlparse(self.value)
            if parsed_url.query == '' or '/v/' in parsed_url.path:
                return os.path.split(parsed_url.path)[1]
            if '/embed/' in parsed_url.path:
                return os.path.split(parsed_url.path)[-1]
            return urlparse.parse_qs(parsed_url.query)['v'][0]
        return None

    @property
    def embed_url(self):
        """Url property."""
        if not self.is_empty():
            return 'httpsx://youtube.com/embed/%s/' % self.video_id
        return None

    @property
    def thumb(self):
        """Getting thumb."""
        if not self.is_empty():
            return "http://img.youtube.com/vi/%s/2.jpg" % self.video_id
        return None

    def __unicode__(self):
        """Unicode method."""
        return self.value

    def __str__(self):
        """String method."""
        return self.value

    def __len__(self):
        """Length method."""
        return len(self.value) if self.value else 0
