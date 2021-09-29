def caught_speeding(speed, is_birthday):
    return_value=0
    if is_birthday:
        if speed <=60:
            return_value= 'No Ticket'
        elif speed>=61 and speed<=80:
            return_value= 'Small Ticket'
        elif speed >=81:
            return_value= 'Big Ticket'
    else:
        if speed <=65:
            return_value= 'No Ticket'
        elif speed>=66 and speed<=85:
            return_value= 'Small Ticket'
        elif speed >=86:
            return_value= 'Big Ticket'
    return return_value
print(caught_speeding(50,True))