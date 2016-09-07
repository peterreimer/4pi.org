#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://beta.4pi.org'
RELATIVE_URLS = False


DELETE_OUTPUT_DIRECTORY = True

PANNELLUM = {'debug' : False,
             'sizes_folder' : 'sizes',
             'tile_folder' : os.path.join(HOME, 'public_html', 'tiles'),
             'tile_url' : 'https://tiles.4pi.org'}

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
