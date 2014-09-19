#!/usr/bin/env python
# coding=utf-8


def normalize_url(url, https=False):
    '''
    author: windows2000
    function:
        add 'http://' or 'https://' prefix to a url if missed
    '''
    if not url:
        return
    elif url.startswith(('http://', 'https://')):
        return url
    if not https:
        url = 'http://' + url
    else:
        url = 'https://' + url
    return url
