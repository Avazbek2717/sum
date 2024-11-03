def stairs(number: int):
    if number == 1:
        return number
    if number == 2:
        return 2
    
    left, right =  1,2
    for i in range(3,number+1):
        left,right = right, left+right
    return right
print(stairs(2))