Title: Setting Up a Pelican Site
Date: 2017-6-4
Category: Coding
Tags: pelican, publishing, webdev, python
Slug: setup-pelican-site
Authors: Adam Li
Summary: A short walkthrough of setting up a pelican site

# Getting Setup with Pelican Site
# By: Adam Li
### Table of Contents
<!-- MarkdownTOC autolink="True" -->

- [Installation](#installation)
    - [1. Conda/Pip Install](#1-condapip-install)
    - [2. Start up pelican:](#2-start-up-pelican)
    - [3. Installing common pelican-themes and pelican-plugins:](#3-installing-common-pelican-themes-and-pelican-plugins)
- [Choosing Your Hosting Server](#choosing-your-hosting-server)
- [Installing and Choosing Themes/Plugins](#installing-and-choosing-themesplugins)
- [Pushing Content to Cloud](#pushing-content-to-cloud)
    - [1. Via Fab \(Old\)](#1-via-fab-old)
    - [2. Via Git Directly](#2-via-git-directly)
- [Adding Pages of Static Content](#adding-pages-of-static-content)
- [Adding Articles To Your Blog](#adding-articles-to-your-blog)
- [Adding Gallery / Images To Your Blog](#adding-gallery--images-to-your-blog)
    - [Modifying Pelican Templates:](#modifying-pelican-templates)
- [References:](#references)

<!-- /MarkdownTOC -->

# Installation
## 1. Conda/Pip Install
After getting your virtualenv setup, run 'pip install pelican'. Also include additional packages:
    
    pip install Markdown beautifulsoup4 typogrify Pillow webassets

or

    conda create -n website python=python3
    conda install -c conda-forge pelican
    conda install -c conda-forge pyaml 
    conda install -c anaconda markdown
    conda install -c anaconda beautifulsoup4 
    conda install -c conda-forge pillow
    conda install -c conda-forge gettext 
    conda install -c damianavila82 piexif # for
    pip install pyexif
    conda install -c conda-forge ghp-import
    conda install -c anaconda pil


for helping to write in Markdown and writing pretty text.

## 2. Start up pelican:
First you will need to create a separate branch that you work on. This branch contains your actual markdown files, which are rendered and then copied OVER to your master branch during the Publishing section. This then renders html using git.

    git checkout - <source_branch>
    pelican-quickstart

then go through the directions and create your project.

## 3. Installing common pelican-themes and pelican-plugins:

    git clone --recursive https://github.com/getpelican/pelican-themes
    git clone --recursive https://github.com/getpelican/pelican-plugins

# Choosing Your Hosting Server
There are a couple of options, but you should decide how you want to host your site because then it will be built into your pelican project directory.

1. Github Pages: This is the free and most convenient way to do things.

2. S3 by Amazon: Costs money.

3. Heroku, PythonAnywhere, and More: 

# Installing and Choosing Themes/Plugins
You need to install the pelican themes and the pelican plugins, if you want to use the open source themes and plugins developed. Then you can add code to your python files to add certain plugins:

	PLUGIN_PATHS = ['path/to/pelican-plugins']
	PLUGINS = ['assets', 'sitemap', 'gravatar']
	JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Pushing Content to Cloud

## 1. Via Fab (Old)
'pip install ghp-import fabric'

1. Using ghp-import:

First run install by 'pip install ghp-import'

Then you can run code like:

    $ ghp-import -m 'commit message' -b master output
    $ git push --all

2. Using fab:

First install fabric by running 'pip install fabric'. Then insert code into your fabfile.py:

    def publishghp(msg):
        preview() #builds publishconf.py
        local("git add -A") #will commit allll files, be careful
        local("git commit -m '%s'"%msg)
        local("ghp-import -m '%s' -b master output"%msg)
        local("git push --all")

and then run 
    
    $ fab publishghp:"commit message"

to create commits up to the cloud.

## 2. Via Git Directly

Before doing anything, check locally if files look right:

    make html && make serve

First just push all your stuff to your path.

    git add -A && git commit -a -m 'first commit' && git push --all

Then:

    make github

# Adding Pages of Static Content
Here you want to add a homepage, about me page and other static pages that are relevant to your site. Create a directory inside /content/pages/ to hold your static pages. Separate blog content and other content and use pelicanconf.py along w/ plugins to play around with the visuals and presentation of the site.

# Adding Articles To Your Blog
To add articles to your blog, create /content/blog/ directory and create subdirectories in there. For example, I have academic, coding, and travel as my subdirectories in my blog. Then adjust your pelicanconf.py file for these blog posts.

# Adding Gallery / Images To Your Blog
Adding images to your blog require the following packages:
- exeif
- Pillow
- Knowledge of modifying Pelican templates

## Modifying Pelican Templates:


https://kwkelly.com/blog/adding-galleries-to-pelican-and-bootstrap/
http://duncanlock.net/blog/2013/05/29/better-figures-images-plugin-for-pelican/

# References:
1. https://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html
2. http://terriyu.info/blog/posts/2013/07/pelican-setup/
3. http://beneathdata.com/how-to/how-i-built-this-website/
4. Pelican-plugins: https://github.com/getpelican/pelican-plugins
5. Pelican-themes: https://github.com/getpelican/pelican-themes
6. Walkthru of Pelican w/ Python3.7: https://rsip22.github.io/blog/create-a-blog-with-pelican-and-github-pages.html