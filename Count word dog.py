def countDog(string):
    listo=list(string.split(' '))
    count=0
    for i in listo:
        if i.lower()=='dog':
           count+=1
    return count
print(countDog('This dog runs faster than the other dog dude!'))