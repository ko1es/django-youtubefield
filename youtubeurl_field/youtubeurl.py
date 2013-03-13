from django.core import validators
import urllib

class YoutubeUrl(object):
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

    def __len__(self):
        return len(self.__unicode__())


def to_python(value):
    if value in validators.EMPTY_VALUES:  # None or ''
        youtube_url = None
    elif value and isinstance(value, basestring):
    	youtube_url = value
    return youtube_url