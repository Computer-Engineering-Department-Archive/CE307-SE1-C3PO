import os
import sys
from app.fixtures.fixtures import *

sys.path.append('/path/to/your/django/app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


if __name__ == '__main__':
    add_category()
    add_channels()
    add_symbols()
