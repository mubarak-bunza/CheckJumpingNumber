def jumping_number(number): 
    if number < 10:
        return "Jumping!!"
    number = str(number)
    l = len(number)
    i=0
    while i < l-1:
        a= i+1
        if abs(int(number[i]) - int(number[a]))!=1:
            return "Not!!"
            break
        i +=1
    
    return "Jumping!!"

print(jumping_number(12634))