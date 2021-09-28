def domainGet(name):
    listo=list(name)
    a=listo.index('@')
    empty_list=[]
    for i in range(len(listo)):
        if(i>a):
            empty_list.append(listo[i])
    combined_list=''.join(empty_list)
    print(combined_list)
print(domainGet('Umair@domain.com'))
