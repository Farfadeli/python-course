chaine = "Hello, world!"
res_dict = {}
for e in chaine: 
    res_dict[e.lower()] += 1
print(res_dict)