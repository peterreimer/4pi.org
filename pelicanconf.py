#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
HOME = os.path.expanduser("~")

AUTHOR = u'Peter Reimer'
SITENAME = u'4pi.org'
SITESUBTITLE = u'Spherical panoramas'
# SITEURL = '/'
# SITEURL = 'http://localhost/~peter/4pi'
SITEURL = 'http://ultra02/~reimer/4pi'
CSS_FILE = 'app.css'
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'
DEFAULT_DATE_FORMAT = '%d.%m.%Y'
STATIC_PATHS = [
    'images',
    'preview',
    'sizes',
    'extras/robots.txt',
    'extras/humans.txt',
    'extras/favicon.ico',
    ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = True
#MENUITEMS = (
#    ('Karte', '/'.join((SITEURL,'karte.html'))),
#)
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
SOCIAL = (('GitHub',    'https://github.com/peterreimer'),
          ('Flickr',    'https://www.flickr.com/photos/4pi'),
          ('Twitter',   'https://twitter.com/4pi'),
          ('360Cities', 'https://www.360cities.net/profile/reimer'),)

#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)


DEFAULT_PAGINATION = 3
# TEMPLATE_PAGES = {'map.html': 'karte.html',}

ARTICLE_URL     = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
# THEME = 'simple'
# THEME = 'pelican-default'
THEME = 'theme'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['neighbors', 'pannellum', 'sitemap']
SITEMAP = {'format': 'xml'}

PANNELLUM = {'debug' : True,
             'autoRotate' : 1,
             'sizes_folder' : 'sizes',
             'tile_folder' : os.path.join(HOME, 'public_html', 'tiles'),
             #'tile_url' : 'http://localhost/~peter/tiles'
             'tile_url' : 'http://ultra02/~reimer/tiles'
             }

JSON_FOLDER = 'json'
SIZES_FOLDER = 'sizes'
FULLSIZE_PANORAMAS = 'panos'

