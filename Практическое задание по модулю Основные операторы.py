result = ''
password = []
n = int(input('Введите число '))
for j in range(1, 20):
    for k in range(1, 20):
        if n % (j + k) == 0 and j < k:
            password.append(j)
            password.append(k)
for i in password:
    result += str(i)
print(result)





