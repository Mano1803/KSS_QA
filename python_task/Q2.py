dict={
    "Name":"MANOJ N",
    2:"813",
    "Place":"Chennai",
    4:"embedur"
}
print(dict)
print("\nKeys")
for key in dict.keys():
    print(key)
print("\n__Values__")
for value in dict.values():
    print(value)
print("\n----Key and value-----")
for key, value in dict.items():
    print(f"{key}: {value}")