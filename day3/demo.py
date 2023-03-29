def magic(counter : int) -> int:
    for idx in range(counter):     # range(0, counter, 1) one value in range(stopping value). start is assumed to be 0 & step is +1
        result=idx ** 2
        yield result #makes function a




#g1 will now become generator
g1 = magic(5)


print(next(g1))

print(next(g1))

print(next(g1))

print(list(g1)) #remaining values

g1 = magic(5) #resetting takes place here!

