# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F403

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://cesararroyo09.github.io"
RELATIVE_URLS = False

# Feed generation for production
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"

# Clean output directory for production builds
DELETE_OUTPUT_DIRECTORY = True

# Production optimizations
LOAD_CONTENT_CACHE = False  # Disable caching for fresh builds
CACHE_CONTENT = False  # Disable content caching
CACHE_PATH = "cache"  # Cache directory (if needed)

# External services (uncomment and configure as needed)
# DISQUS_SITENAME = "your-disqus-sitename"
# GOOGLE_ANALYTICS = "UA-XXXXXXXXX-X"  # or GA4: "G-XXXXXXXXXX"

# Social media and SEO
# TWITTER_USERNAME = "your-twitter"
# FACEBOOK_APP_ID = "your-facebook-app-id"

# Security headers and meta tags for production
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
# }

# Production-specific plugins (if any)
# PLUGINS = PLUGINS + ['sitemap', 'seo']  # Add to existing plugins

# Sitemap configuration
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 0.5
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
# }
