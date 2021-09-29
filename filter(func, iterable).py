a=[10,20,30,50,60,80,70,400]

def func(n):
    if n>50:
        return True

filtered_elements=filter(func,a)
print(filtered_elements)

for i in filtered_elements:
    print(i)

print('\n')

filtered_elements1=filter(lambda n:(n>50),a)
for a in filtered_elements1:
    print(a)