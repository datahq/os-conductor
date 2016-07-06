import os

# from werkzeug.contrib.cache import MemcachedCache, SimpleCache

from .models import query

# TODO: Add caching to reults (not so simple since we want
#      to immediately show new datasets)
# if 'OS_CONDUCTOR_CACHE' in os.environ:
#     cache = MemcachedCache([os.environ['OS_CONDUCTOR_CACHE']])
# else:
#     cache = SimpleCache()


def search(kind, userid, args={}):
    """Initiate an elasticsearch query
    """
    hits = query(kind, userid, **args)
    return hits
