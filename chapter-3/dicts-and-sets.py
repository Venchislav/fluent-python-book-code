# Pretty nice example of using dicts on maximum
# dictionary embedding - IDK i used Google Translate :)
dial_codes = [(880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

contry_dial = {country: code for code,country in dial_codes}
print(contry_dial)


# Connection by |

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

print(d1 | d2)
print(d1)

# As u can see d1 didn't chage
# But we can fix it...

d1 |= d2
print(d1)

food = dict(category='ice cream', flavor='vanilla', cost=199)

match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')
# Sonic's advice:
# Object must be hashible (constant) and must contain only hashible (constant) elems
