def roman2(nums: int)->str:
    r_a = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            
            4:'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'   
        }

    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9,5, 4, 1]

    result = ''
    i = 0
    while nums:
        if numbers[i] <= nums:
            result+=r_a[numbers[i]]
            nums=nums-numbers[i]
        else:
            i = i +1
    return result
print(roman2(1000))