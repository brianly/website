# -*- encoding: utf-8 -*-
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'Brian Lyttle'
WWW_ROOT = 'http://www.brianlyttle.com'
CDN_ROOT = 'http://cdn.brianlyttle.com'

AUTHOR = 'Brian Lyttle'
EMAIL = 'blog@brianlyttle.com'

FILTERS = ['markdown+codehilite(css_class=highlight)',
           'hyphenate', 'h1']
VIEWS = {
    # Home
    '/': {'view': 'index',
          'pagination': '/page/:num/',
          'items_per_page': 4,
          'template': 'main.html'},

    # Individual posts
    '/:year/:month/:slug/': {'view': 'entry',
                             'template': 'post.html'},

    # Monthly archives
    '/:year/:month/': {'view': 'archive',
                       'template': 'archive.html'},

    # Tags
    '/tag/:name/': {'view': 'tag',
                    'pagination': '/tag/:name/:num',
                    'template': 'tag.html'},

    # Pages
    "/:slug/": {'view': 'page',
                'template': 'page.html'},

    # Feeds
    '/feed/atom/': {'filters': ['h2', 'nohyphenate'],
                    'view': 'atom'},
    '/feed/': {'filters': ['h2', 'nohyphenate'],
               'view': 'rss'},

    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'],
    #                      'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'],
    #                     'view': 'rsspertag'},

    # Sitemap
    '/sitemap.xml': {'view': 'sitemap'},

    # More examples

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

DEPLOYMENT = {
    "ls": "ls $OUTPUT_DIR",
    "echo": "echo '$OUTPUT_DIR'",
    "production": "rsync --verbose -av $OUTPUT_DIR brianly@brianlyttle.com:~/sites/blweb/www",
    "default": "rsync --verbose -av $OUTPUT_DIR brianly@brianlyttle.com:~/sites/beta/www"
}
