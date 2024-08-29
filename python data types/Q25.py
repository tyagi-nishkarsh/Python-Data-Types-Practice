d1 = {
     "a" : "tiago",
     "b" : 2018,
     "c" : 4542,
}

d2 = {
    "a" : "joker",
    "b" : 2015,
    "c" : 143,
}
d3=(dict(d1))
d3.update(d2)
print(d3)

for key in d2:
    if key in d1:
        d2[key] = d2[key] + d1[key]
    else:
        pass

print(d2)