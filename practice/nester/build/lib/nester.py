movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gialliam", "Eric Idle", "Terry Jones"]]]
print(movies)
print("-------------------------")
def show(items):
    for each_item in items:
        if isinstance(each_item, list):
            show(each_item)
        else:
            print(each_item)

show(movies)

print("+++++++++++++++++++++++")
def normalize(x):
    return x.capitalize()


r = map(normalize, ['adam', 'LISA', 'barT'])
print(list(r))

from functools import reduce
def prod(x, y):
    return x * y
r1 = reduce(prod, [3, 5, 7, 9])
print(r1)



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L))

def mysort(x):
    return x[1] > y[1]

from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key= lambda item:item[1], reverse=True))
print(sorted(L, key=itemgetter(1,0), reverse=True))