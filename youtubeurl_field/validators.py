#-*- coding: utf-8 -*-
import re
import urllib2
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import  forms
from django.core.validators import EMPTY_VALUES

def validate_youtube_url(value):
    '''El patron lo saque de http://stackoverflow.com/questions/2964678/jquery-youtube-url-validation-with-regex'''
    pattern = r'^http:\/\/(?:www\.)?youtube.com\/watch\?(?=.*v=\w+)(?:\S+)?$'
    
    if not value.is_empty():
        con = urllib2.urlopen(value.value)
        if con.code != 200:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        if value.value[:16] == 'http://youtu.be/':
            if re.match(r'\w+', value.value[16:]) is None:
                raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        elif re.match(pattern, value.value) is None:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
