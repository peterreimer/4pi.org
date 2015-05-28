#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Peter Reimer'
SITENAME = u'4pi.org'
#SITESUBTITLE = u'Spherical panoramas'
SITEURL = ''
#SITEURL = 'http://4pi.org'
CSS_FILE = '4pi.css'
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'
STATIC_PATHS = [
    'images',
    'preview', 
    'extras/robots.txt',
    'extras/humans.txt',
    'extras/favicon.ico',
    ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = True
MENUITEMS = (
    ('Karte', 'karte.html'),
)
# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('PanoTools.org Wiki', 'http://wiki.panotools.org'),
          ('Hugin', 'http://hugin.sourceforge.net/'),)

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path':'robots.txt'},
    'extras/humans.txt': {'path':'humans.txt'},
    'extras/favicon.ico': {'path':'favicon.ico'},
    }   
# Social widget
SOCIAL = (('GitHub', 'https://github.com/peterreimer'),
          ('Delicious','https://delicious.com/preimer'),
          ('360Cities', 'http://www.360cities.net/profile/reimer'),)

DEFAULT_PAGINATION = 10
TEMPLATE_PAGES = {'map.html': 'karte.html'}

ARTICLE_URL     = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
# THEME = 'simple'
# THEME = 'pelican-default'
# THEME = '4pi-theme'
THEME = 'foundation-salado'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["neighbors", "gps", "pannellum"]

PANORAMA_PREVIEW_PATH = 'preview'
JSON_FOLDER = 'json'
TILE_FOLDER = 'tiles'
PANNELLUM_DEBUG = True
# PANNELLUM_DEBUG = False
FULLSIZE_PANORAMAS = 'panos'

