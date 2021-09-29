#variables before (:) are arguments while elements after (:) are expressions

add=lambda x,y:x+y
print(add(555,100))

add_subtract=lambda x,y:(x+y,x-y)
add,subtract=add_subtract(10,5)
print(add)
print(subtract)