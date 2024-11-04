def str_sum(word: str):
    result = ""
    count = 1
    for i in range(1,len(word)):
        if word[i] == word[i-1] and count != 9:
            count+=1
        else:
            result+=f'{count}{word[i-1]}'
            count = 1
    result+=f'{count}{word[-1]}'
    return result

print(str_sum("aaaaaaaaaaaaaabb"))