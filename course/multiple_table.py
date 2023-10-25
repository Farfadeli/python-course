def without_double(number):
    res = [];
    for e in range(len(number)):
        if(number[e] in number[e+1:len(number)]):
            continue
        res += [number[e]]
    return res
test = [1,2,3,4,2,6,4,1]
print(without_double(test))

number = int(input("Choississer la table que vous voulez : "))
res = []
for i in range(1, 11):
    res += [str(i*number)+'*'] if (i*number) % 3 == 0 else [i*number]
print(res)
