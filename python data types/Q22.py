listt = [
    ("tiago", 2018),
    ("jupiter", 2015),
    ("Yamaha", 2013),
    ("Bike", 2016),
    ("TV", 2022)
]

listt.sort(key=lambda tup: tup[1])
print(listt)
listt.sort(key=lambda tup: tup[1] , reverse=True)
print(listt)

