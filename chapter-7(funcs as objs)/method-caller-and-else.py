from operator import methodcaller, mul
from functools import partial
from tags import tag

upcase = methodcaller('upper')
print(upcase('this str will be uppercased'))

triple = partial(mul, 3)
print(triple(5))

htmlizer = partial(tag, 'img', class_='logo')
print(htmlizer(src='cat.png'))
