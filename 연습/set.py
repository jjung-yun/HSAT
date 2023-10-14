print(dir({1}))

a={1,2,3}
b={2,3,4}

print("a|b=합집합",a|b, a.union(b))
print("a&b=교집합",a&b, a.intersection(b))
print("a-b=ck집합",a-b, a.difference(b))
print("a^b=대칭차집합",a^b, a.symmetric_difference(b))