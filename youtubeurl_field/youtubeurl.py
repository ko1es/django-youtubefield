import urllib2
import urlparse
import os
from django.core import validators


class YoutubeUrl(unicode):

    @property
    def video_id(self):
        parsed_url = urlparse.urlparse(self)
        if parsed_url.query == '' or '/v/' in parsed_url.path:
            return os.path.split(parsed_url.path)[1]
        return urlparse.parse_qs(parsed_url.query)['v'][0]
 
    @property
    def embed_url(self):
        return 'http://youtube.com/embed/%s/' % self.video_id

    def is_valid(self):
        try:
            con = urllib2.urlopen(self)
            return True if con.code == 200 else False
        except:
            return False

    @property
    def thumb(self):
        return "http://img.youtube.com/vi/%s/2.jpg" % self.video_id


def to_python(value):
    if value in validators.EMPTY_VALUES:  # None or ''
        youtube_url = None
    elif value and isinstance(value, basestring):
        youtube_url = YoutubeUrl(value)
    return youtube_url