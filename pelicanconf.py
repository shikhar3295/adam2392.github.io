#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml
from collections import namedtuple
def convert(dictionary):
	return namedtuple("Image", dictionary.keys())(**dictionary)

# 
AUTHOR = "Adam Li"
SITENAME = "Adam Li's blog"
SITEURL = "https://adam2392.github.io"
SITETITLE = "Adam J. Li"
COPYRIGHT_YEAR = 2019

PATH = "content"

# Photo blog settings | https://github.com/getpelican/pelican-plugins/tree/master/photos
# PHOTO_LIBRARY = "~/Pictures"
# PHOTO_GALLERY = (4288, 2848, 100)	# For photos in galleries, maximum width and height, plus JPEG quality
# PHOTO_ARTICLE = (760, 506, 80)	# For photos associated with articles, maximum width, height, and quality
# PHOTO_THUMB = (192, 144, 60)	# For thumbnails, maximum width, height, and quality
# PHOTO_RESIZE_JOBS = 5 			# Number of parallel resize jobs to be run.
# PHOTO_WATERMARK = True # Adds a watermark to all photos in articles and pages. Defaults to using your site name.
# PHOTO_WATERMARK_TEXT = "ADAM LI" # Allow the user to change the watermark text or remove it completel
# PHOTO_EXIF_KEEP = True
# PHOTO_EXIF_REMOVE_GPS = True  # Removes any GPS information from t
# PHOTO_EXIF_COPYRIGHT = "COPYRIGHT"
# PHOTO_EXIF_COPYRIGHT_AUTHOR = "Adam Li"

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
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"
RSS_FEED_SUMMARY_ONLY = False

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# to run the theme | for now, pelican-bootstrap3
THEME = "pelican-themes/pelican-bootstrap3"
# THEME = "pelican-themes/Responsive-Pelican"
PLUGIN_PATHS = ["pelican-plugins"] 
PLUGINS = [
"i18n_subsites",
 "render_math", "related_posts", "photos", \
"pelican_javascript"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Main page
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (("Blog", "/categories.html"),
             ("Timeline", "/archives.html"),
             ("Tags", "/tags.html"),
             ("Curriculum Vitae", "/pdfs/AdamLi_CV.pdf"),
              # ("Blog", "/blog.html"),
             # ("Gallery", "/gallery.html"),
             )

# Blogroll
# LINKS = (("Pelican", "http://getpelican.com/"),)

# Social widget
GITHUB_URL = "https://github.com/adam2392"
GITHUB_USER = "adam2392"
TWITTER_USERNAME = "adam2392"
SOCIAL = (("twitter", "https://twitter.com/adam2392"),
		      ("stack-overflow", "https://stackexchange.com/users/4494355/ajl123"),
          ("github", "https://github.com/adam2392"),
          ("linkedin", "https://www.linkedin.com/in/adam2392"))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static content
STATIC_PATHS = ["pdfs", "files", "photos"]

# Google Analytics Tag
GOOGLE_ANALYTICS ="UA-106551801-1"
