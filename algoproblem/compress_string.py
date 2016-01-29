arr = 'aaaabbbbccceeappppppp'
def compress_string(string):
    result =''
    count =1
    string = string + '\0'
    for i in range(1,len(string)):
        if string[i-1] ==string[i]:
            count+=1
        else:
            result += string[i-1]+str(count)+compress_string(string[i:])
            break
    return result

print(compress_string(arr))
