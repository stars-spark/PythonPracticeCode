#
myfriends = ['a', 'b', 'c', 'd']
print(myfriends)

#one of my friends did not come
missfriend = myfriends.pop(-1)
print(missfriend)
myfriends.insert(-1, 'e')
print("Welcome to my party, " + myfriends[0])
print("Welcome to my party, " + myfriends[1])
print("Welcome to my party, " + myfriends[2])
print("Welcome to my party, " + myfriends[3])

print("I found a bigger table,It can have more people")
myfriends.insert(0, 'x')
myfriends.insert(2, 'y')
myfriends.append('z')
print("I invite x")
print("I invite y")
print("I invite z")

print("I am so sorry,I can only invite two friends")

one = myfriends.pop()
print(one)