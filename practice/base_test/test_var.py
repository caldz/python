a='asdf'
b=a
print(id(a),id(b),a,b)
a='1111'
print(id(a),id(b),a,b)

a=1
b=a
print(id(a),id(b),a,b)
a+=5
print(id(a),id(b),a,b)

a={1,2,3,4,1}
b=a
print(id(a),id(b),a,b)
a.add(6)
print(id(a),id(b),a,b)

input()