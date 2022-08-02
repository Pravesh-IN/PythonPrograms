def greet(name, time='morning'):
    return f'Hello {name}, Good {time}'

def intro(name, profession):
    return f'My name is {name} and My profession is {profession}'


print(greet('John','Evening'))

wish=greet


funct= [wish, greet, str.lower, str.capitalize, intro]

for f in funct:
    print(f.__name__)
    print(f)
