def findDog(string):
   listo=list(string.split(' '))
   for i in listo:
        if i=='dog':
            return True
   else:
            return False

print(findDog('Is there any dog here?'))