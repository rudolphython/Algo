words = str(input())
check = str(input())

result = 0
i = 0
while i <= len(words) - len(check):
    flag = 0
    for j in range(len(check)):
        if words[i+j] == check[j]:
            flag += 1
        else:
            i += 1
            break
        if flag == len(check):
            result += 1
            i += len(check)



print(result)
