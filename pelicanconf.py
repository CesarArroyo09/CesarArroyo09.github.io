AUTHOR = "César Arroyo"
SITENAME = "César Arroyo"
SITESUBTITLE = "Studied Physics (master), now I work on Data Engineering and AI"
SITEIMAGE = "images/profile.png width=160 height=160"
SITEURL = "https://cesararroyo09.github.io"

AUTHOR_EMAIL = "cesararroyocardenas@gmail.com"
DESCRIPTION = (
    "Builder. Working at the intersection of data engineering, analytics and AI. My "
    "background is in Physics where I worked with mock galaxy catalogs. My current "
    "interests are docker, python, deep learning, data engineering and programming."
)
PATH = "content"

TIMEZONE = "America/Mexico_City"

DEFAULT_LANG = "en"

THEME = "themes/pelican-alchemy/alchemy"
BOOTSTRAP_CSS = (
    "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/litera/bootstrap.min.css"
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


ICONS = (
    ("github", "https://github.com/cesararroyo09"),
    ("linkedin", "https://linkedin.com/in/cesar-arroyo-cardenas"),
    ("fas fa-envelope", "mailto:cesararroyocardenas@gmail.com"),
)

PYGMENTS_STYLE = "friendly"

FOOTER_LINKS = [
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
    # ("buy me a coffee", "https://www.buymeacoffee.com/cesararroyo09"),
]

DEFAULT_PAGINATION = 10

ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}.html"
PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}.html"

STATIC_PATHS = ["images", "extras"]

# Favicon configuration (Real Favicon Generator)
# RFG_FAVICONS = True
# EXTRA_PATH_METADATA = {
#     "extras/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
#     "extras/favicon-32x32.png": {"path": "favicon-32x32.png"},
#     "extras/favicon-16x16.png": {"path": "favicon-16x16.png"},
#     "extras/favicon.ico": {"path": "favicon.ico"},
#     "extras/site.webmanifest": {"path": "site.webmanifest"},
#     "extras/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
#     "extras/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
# }

RELATIVE_URLS = True
HIDE_AUTHORS = True
