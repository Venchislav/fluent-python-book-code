# Good
colors = ['black', 'white', 'red', 'blue']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
           for size in sizes]
print(tshirts)

print('-----------')
# But It's God Mode

colors = ['black', 'white', 'red', 'blue']
sizes = ['S', 'M', 'L']

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)