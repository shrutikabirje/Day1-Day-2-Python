Iterate a given list and check if a given element already exists in a dictionary as a key’s value if not delete it from the list.



l=[1,23,56,67,34,45,87]
d={"shru":23,"adii":67,"yasu":46,"Maria":45}
for i in l:
    for j in d.values():
        if i==j:
            l.remove(i)
print("edited list is:",l)
        

