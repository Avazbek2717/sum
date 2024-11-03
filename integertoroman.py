def roman2(number:int) ->str:
    d = {
         1:	 'I',
        5:	  'V',
        10:	   'X',
        50:    'L',
        100:    'C',
        500:	'D',
        1000:	'M',
    }
    result = ''
    for i in d:
        result+=str(d[i])
    return result

print(roman2(number=1))
    
