# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'Brian Lyttle'
WWW_ROOT = 'http://www.brianlyttle.com'

AUTHOR = 'Brian Lyttle'
EMAIL = 'blog@brianlyttle.com'

FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']
VIEWS = {
    '/': {'filters': 'summarize',
          'view': 'index',
          'pagination': '/page/:num',
          'items_per_page': 5},

    '/:year/:month/:slug/': {'view': 'entry',
                    'template': 'archive.html'},

    '/tag/:name/': {'filters': 'summarize',
                    'view':'tag',
                    'pagination': '/tag/:name/:num'},

    # per tag Atom or RSS feed. Just uncomment to generate them.

    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/feed/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/feed/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    # '/articles/': {'view': 'articles'},

    '/sitemap.xml': {'view': 'sitemap'},

    "/:slug/": {"view": "page",
                'template': 'page.html'},

    # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    # '/:slug/': {'view': 'page'}

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags}

    # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown'],
    #                  'view': 'entry'}
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%Y-%m-%d %H:%M'
SUMMARIZE_LINK = '<span>&#8230; <a href="%s" class="continue">Continue reading</a></span>'
