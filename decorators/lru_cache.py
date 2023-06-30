# LRU_cache = Least Recently Used
# That means that it removes elements, that haven't been called for a long time
# It saves memory usage and has a max_size param
from functools import lru_cache

# maxsize - max amount of elems in cache
# typed - should we divide cache on type groups


@lru_cache(maxsize=2**20, typed=True)
def costly_used(a, b):
    return a, b
