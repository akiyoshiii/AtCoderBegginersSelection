N, A, B = map(int, input().split())

answer = 0

list = [] #何らかの位の数字を格納

for i in range(1, N + 1 ):
    j = i
    while ( j > 0):
        list.append(j % 10)
        j = j // 10
    x = sum(list)
    list = []
    if x >= A and x <= B:
        answer+= i

print(answer)

