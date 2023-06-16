# It's about match case with dicts

request = {'url': 'https://www.youtube.com/', 'method': 'GET', 'timeout':1000}

# Works only if we have le 3 elems in dict, and url and method are strs
match request:
    case {'url': str() as url, 'method': str() as method} if len(request) <= 3:
        print(f'{url}: {method}')
    case _:
        print('Wrong request homie💀')

# or
# This works with kwargs. Only if we have le 2 additional elems in dict
match request:
    case {'url': str() as url, 'method': str() as method, **kw} if len(kw) <= 2:
        print(f'{url}: {method}')
    case _:
        print('Wrong request homie💀')