#-*- coding: utf-8 -*-
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_youtube_url(value):
    '''El patron lo saque de http://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex'''
    pattern = r'^http:\/\/(?:www\.)?youtube.com\/watch\?(?=.*v=\w+)(?:\S+)?$'
 
    if value[:16] == 'http://youtu.be/':
        if re.match(r'\w+', value[16:]) is None:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
    elif re.match(pattern, value) is None:
        raise forms.ValidationError(_(u'Not a valid Youtube URL'))