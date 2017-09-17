Title: Setting Up a Pelican Site
Date: 2017-6-4
Category: Python
Tags: pelican, publishing, webdev, python
Slug: setup-pelican-site
Authors: Adam Li
Summary: A short walkthrough of setting up a pelican site

# Getting Setup with Pelican Site
# By: Adam Li
<!-- MarkdownTOC -->

- Installation
- Choosing Your Hosting Server
- Installing and Choosing Themes/Plugins
- Pushing Content to Cloud
- Adding Pages of Static Content
- Adding Articles To Your Blog
- References:

<!-- /MarkdownTOC -->

# Installation
1. After getting your virtualenv setup, run 'pip install pelican'. Also include additional packages:

'pip install Markdown beautifulsoup4 typogrify Pillow webassets'

for helping to write in Markdown and writing pretty text.

# Choosing Your Hosting Server
There are a couple of options, but you should decide how you want to host your site because then it will be built into your pelican project directory.

1. Github Pages

2. S3 by Amazon

3. Heroku, PythonAnywhere, and More

# Installing and Choosing Themes/Plugins
You need to install the pelican themes and the pelican plugins, if you want to use the open source themes and plugins developed.

Go to these two websites to get your themes/plugins.
https://github.com/getpelican/pelican-themes
https://github.com/getpelican/pelican-plugins

Afterwards, you can follow those instructions to get a certain theme setup. 

Clone:

	git clone https://github.com/getpelican/pelican-themes.git
	git clone https://github.com/getpelican/pelican-plugins

Then:

	PLUGIN_PATHS = ['path/to/pelican-plugins']
	PLUGINS = ['assets', 'sitemap', 'gravatar']

	JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


# Pushing Content to Cloud
'pip install ghp-import fabric'

1. Using ghp-import
First run install by 'pip install ghp-import'

Then you can run code like:

    $ ghp-import -m 'commit message' -b master output
    $ git push --all

2. Using fab

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

# Adding Pages of Static Content
Here you want to add a homepage, about me page and other static pages that are relevant to your site.


# Adding Articles To Your Blog

# References:
1. https://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html
2. http://terriyu.info/blog/posts/2013/07/pelican-setup/
3. http://beneathdata.com/how-to/how-i-built-this-website/
