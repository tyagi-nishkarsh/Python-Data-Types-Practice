dict = {
    "a" : "apple",
    "b" : "banana",
    "c" : "cat",
    "d" : "dog",
    "e" : "elephant"

}

if "a" in  dict:
    print("a")
if "f" in dict:
        print("f")
else:
    print("no such key")

dict.pop("b")
print(dict)
