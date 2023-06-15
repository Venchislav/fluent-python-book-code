a = [1, 2, 3, 4, 5]
print(a[3:]) # all elements since 3rd
print(a[:3]) #all elements before 3rd

print(a[::2]) # Each 2nd element
print(a[::-1]) # Each 1st element in reversed arr - reverese arr

print(a[::-2]) # Each 2n element in reversed arr


# To make slice of 2d arr we use
# a[m:n, k:l] construction

# We can also make some operations with slices

a = list(range(0, 100, 10))
print(f'Before del slice - {a}')


del a[5:7]

print(f'After del slice - {a}')

print('------------------\n')

a = list(range(0, 100, 10))
print(f'Before changes slice - {a}')
a[2:5] = [100]
# But not a[2:5] = 100 !!!!!
print(f'After changes slice - {a}')