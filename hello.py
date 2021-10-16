def make_incrementor(n):
    return lambda x:x+n
f=make_incrementor(42)
print(f(0))
print(f(1))
print(f(42))

print()

pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)
pairs.sort(key=lambda pair:pair[0])
print(pairs)

print()

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
print(my_function.__doc__)

print()

def mix(fruit:str,vegetable:str='potato')->str:
    print('annotations',mix.__annotations__)
    print('arguments:',fruit,vegetable)
    return fruit+' and '+vegetable
print(mix('apple'))