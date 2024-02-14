AUTHOR = "Atul Vinayak"
SITENAME = "a.tulv.in"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

THEME = "oaitheme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/avinayak"),
    ("LinkedIn", "https://www.linkedin.com/in/atulvinayak"),
    ("Instagram", "https://www.instagram.com/avinayak__"),
    ("BlueSky", "https://bsky.app/profile/a.tulv.in"),
    ("Twitter", "https://twitter.com/atulvinayak"),
)

# Social widget
ABOUT = (
    ("Resume", "https://goo.gl/D2GXJ9"),
    ("Photography", "https://unsplash.com/collections/519921/s'ok-pics"),
    ("Visual References", "https://v.tulv.in"),
    ("Ko-fi", "https://ko-fi.com/atulvinayak"),
)


DEFAULT_PAGINATION = 10000

STATIC_PATHS = ["media"]
PLUGINS = ["pelican.plugins.render_math"]

MATH_JAX = {"color": "blue", "align": "left"}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
