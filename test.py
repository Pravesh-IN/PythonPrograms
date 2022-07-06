def greet(name, time='morning'):
    return f'Hello {name}, Good {time}'

print(greet('John','Evening'))

wish=greet
#del greet

funct= [wish, greet, str.lower, str.capitalize]

for f in funct:
    print(f.__name__)
