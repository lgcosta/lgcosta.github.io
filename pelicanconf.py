#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Luiz Gustavo Costa'
SITENAME = u'Blog GugaBSD'
SITEURL = 'http://luizgustavo.pro.br/blog/'
STATIC_PATHS = ['images']
#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MD_EXTENSIONS = ['codehilite','extra']
PLUGINS = ['pelican_youtube']
PATH = 'content'
THEME = 'themes/pelican-bootstrap3'
GOOGLE_ANALYTICS = 'UA-42026281-1'
BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'monokai'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
    )

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/gugabsd'),
    ('Facebook', 'http://facebook.com/gugabsd')
)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'gugabsd'
#DISQUS_NO_ID = True
#DISQUS_ID_PREFIX_SLUG = True
DISQUS_DISPLAY_COUNT = True
TWITTER_USERNAME = 'gugabsd'
GITHUB_URL = 'lgcosta'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
