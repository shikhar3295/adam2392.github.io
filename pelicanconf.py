#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Li'
SITENAME = u"Adam Li's Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# to run the theme 
# for now, pelican-bootstrap3
# THEME = 'pelican-themes/pelican-bootstrap3'
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# PLUGIN_PATHS = ['/path/to/git/pelican-plugins'] 
# PLUGINS = ['i18n_subsites']
THEME = "pelican-themes/Flex/"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Main page
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (("Blog", "/blog.html"),
             ("Archives", "/archives.html"),
             ("Categories", "/categories.html"),
             ("Tags", "/tags.html"),)

# Social widget
GITHUB_URL = "https://github.com/adam2392"
TWITTER_USERNAME = "adam2392"
SOCIAL = (("twitter", "https://twitter.com/adam2392"),
          ("github", "https://github.com/adam2392"),
          ("linkedin", "https://www.linkedin.com/in/adam2392"))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
