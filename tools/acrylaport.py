import os
import codecs
import xml.etree.ElementTree as etree

from dateutil import parser as du
from urlparse import urlparse


def parse_export(path):
    """Parses the WordPress export file into a Python-native format"""
    posts = []
    tree = etree.parse(path)
    root = tree.getroot()

    for item_elem in root.iter('item'):
        # Stash this in case it might be useful
        post = {'_raw': item_elem.getchildren()}

        # Include only the useful stuff
        for i in item_elem.getchildren():
            if i.tag == 'category':
                if 'tags' not in post:
                    post['tags'] = []
                if i.attrib['domain'] == 'post_tag': # only capture tags - not categories
                    post['tags'].append(i.attrib['nicename'])
            elif i.tag == 'link':
                post['url'] = i.text
            elif i.tag == 'pubDate':
                post['published'] = unicode(du.parse(i.text))
            elif i.tag == 'title':
                post[i.tag] = i.text
            elif i.tag == '{http://purl.org/rss/1.0/modules/content/}encoded':
                post['content'] = i.text
            elif i.tag == '{http://wordpress.org/export/1.2/}status':
                post['status'] = i.text

        posts.append(post)

    return posts

OUTPUT_DIR = os.path.join(os.getcwd(), 'out')
INDEX_NAME = 'index.txt'

posts = parse_export('wordpress-exports/brianlyttle.wordpress.2013-01-12.postsonly.xml')

for p in posts:
    if p['status'] == 'publish':
        title = 'title: "%s"\n' % p['title']
        date = 'date: %s\n' % (unicode(p['published'])[0:16])
        tags = 'tags: [%s]\n' % ', '.join(p['tags'])

        text = ''.join(['---\n', title, date, tags, '---\n', p['content']])

        post_path = os.path.join(OUTPUT_DIR, urlparse(p['url']).path[1:])
        if not os.path.exists(post_path):
            os.makedirs(post_path)

            with codecs.open(os.path.join(post_path, INDEX_NAME), 'w', 'utf-8') as f:
                f.write(text)