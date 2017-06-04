#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# jinja2.Environment.install_gettext_callables

AUTHOR = u'Adam Li'
SITENAME = u"Adam Li"
SITEURL = 'http://localhost:8000'
# SITELOGO = 
SITETITLE = 'Adam J. Li'
COPYRIGHT_YEAR = 2017
HEADER_IMAGE='header.JPG'

PATH = 'content'

# # Photo blog settings | https://github.com/getpelican/pelican-plugins/tree/master/photos
# PHOTO_LIBRARY = 'photos'
# PHOTO_GALLERY = (1024, 768, 80)	# For photos in galleries, maximum width and height, plus JPEG quality
# PHOTO_ARTICLE = (760, 506, 80)	# For photos associated with articles, maximum width, height, and quality
# PHOTO_THUMB = (192, 144, 60)	# For thumbnails, maximum width, height, and quality
# PHOTO_RESIZE_JOBS = 5 			# Number of parallel resize jobs to be run.
# # PHOTO_WATERMARK = True # Adds a watermark to all photos in articles and pages. Defaults to using your site name.
# # PHOTO_WATERMARK_TEXT = 'ADAM LI' # Allow the user to change the watermark text or remove it completel

# PHOTO_EXIF_KEEP = True
# PHOTO_EXIF_REMOVE_GPS = True  # Removes any GPS information from t
# PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'
# PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Adam Li'

# Handling Articles
INDEX_SAVE_AS = "blog.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

RELATED_POSTS_MAX = 10

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# to run the theme | for now, pelican-bootstrap3
THEME = 'pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['plugins'] 
PLUGINS = ['i18n_subsites', 'render_math', 'related_posts']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# THEME = "pelican-themes/Flex/"

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Main page
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (("Blog", "/blog.html"),
             ("Archives", "/archives.html"),
             ("Categories", "/categories.html"),
             ("Curriculum Vitae", "/pdfs/AdamLi_CVFellowships.pdf"),
             ("Tags", "/tags.html"),)

# Social widget
GITHUB_URL = "https://github.com/adam2392"
GITHUB_USER = 'adam2392'
TWITTER_USERNAME = "adam2392"
SOCIAL = (("twitter", "https://twitter.com/adam2392"),
		  ("stack-overflow", "https://stackexchange.com/users/4494355/ajl123"),
          ("github", "https://github.com/adam2392"),
          ("linkedin", "https://www.linkedin.com/in/adam2392"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Static content
STATIC_PATHS = ["pdfs", "files"]
