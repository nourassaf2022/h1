num = int(input('Number: '))
binary = []
while num > 0:
    binary.append(num%2)
    num=num//2
for i in range(len(binary)):
    print(binary[-i-1], end='')