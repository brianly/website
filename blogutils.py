import os
import random
import string
import shutil

def nonce():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(9))

def invalidate_css(css_file):
    css_src = os.path.join(os.getcwd(), 'theme/stylesheets/app.css')
    css_dest = os.path.join(os.getcwd(), 'theme/stylesheets/', css_file)
    shutil.copy(css_src, css_dest)
