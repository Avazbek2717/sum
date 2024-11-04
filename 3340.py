'''Input: num = "1234"

Output: false

'''

def num_add(num: str):
    j = 0
    t = 0
    for i in range(0,len(num),2):
        j = j+int(num[i])
    for h in range(1,len(num),2):
        t =t+int(num[h])
    if j == t:
        return True
    else:
        return False

print(num_add('2412'))

