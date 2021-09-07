from pprint import pprint

a = [1,4,2,7,1,9,0,3,4,6,6,6,8,3]
z = ["a", "b", "c"]
numList = ['1', '2', '3', '4']


print(a[::-1])
print(a[-2])
print(a[::-2])
print(z)
pprint(z)

listef=["{}{}".format(i,j) for i in a for j in z]

print(listef)

lambda_func = lambda hello, world: print(hello, end=' ') or print(world)

lambda_func('Hello', 'World!')