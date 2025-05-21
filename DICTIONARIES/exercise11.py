my_family = {
    "child1": {
        "name": "Emily",
        "age": 5
    },
    "child2": {
        "name": "John",
        "age": 8
    },
    "child3": {
        "name": "Lisa",
        "age": 3
    }
}
print(my_family["child1"]["name"])  
for child, info in my_family.items():
    print(child)
    for key in info:
        print(key, ":", info[key])
    print()