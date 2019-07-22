#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml
from collections import namedtuple
def convert(dictionary):
	return namedtuple("Image", dictionary.keys())(**dictionary)

# 
AUTHOR = 'Adam Li'
SITENAME = "Adam Li's blog"
SITEURL = 'https://adam2392.github.io'
SITETITLE = 'Adam J. Li'
COPYRIGHT_YEAR = 2019

PATH = 'content'

# Photo blog settings | https://github.com/getpelican/pelican-plugins/tree/master/photos
# PHOTO_LIBRARY = '~/Pictures'
# PHOTO_GALLERY = (4288, 2848, 100)	# For photos in galleries, maximum width and height, plus JPEG quality
# PHOTO_ARTICLE = (760, 506, 80)	# For photos associated with articles, maximum width, height, and quality
# PHOTO_THUMB = (192, 144, 60)	# For thumbnails, maximum width, height, and quality
# PHOTO_RESIZE_JOBS = 5 			# Number of parallel resize jobs to be run.
# PHOTO_WATERMARK = True # Adds a watermark to all photos in articles and pages. Defaults to using your site name.
# PHOTO_WATERMARK_TEXT = 'ADAM LI' # Allow the user to change the watermark text or remove it completel
# PHOTO_EXIF_KEEP = True
# PHOTO_EXIF_REMOVE_GPS = True  # Removes any GPS information from t
# PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'
# PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Adam Li'

# # handling the gallery
# with open("./images.yaml", "r+") as f:
# 	IMAGES = convert(yaml.load(f.read()))

# TEMPLATE_PAGES = {
#     "gallery.html": "gallery.html",
# }

# Handling Articles
INDEX_SAVE_AS = "blog.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"
RELATED_POSTS_MAX = 5

# language/time settings
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True