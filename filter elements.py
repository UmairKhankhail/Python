seq = ['soup','dog','salad','cat','great']
x=lambda n: not (n.startswith('s'))
filtered_elements=filter(x,seq)
for i in filtered_elements:
    print(i)