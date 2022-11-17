count = 0 #何回処理ができたか
end = 0 #2で割れない数字があると増える

#入力の格納
n = int(input()) # 数字がいくつあるか
l = list(map(int, input().split())) # 数字の入力

while True:
    for i in range(n):
        if l[i] % 2 != 0:
            end += 1
            break
        else:
            l[i] = l[i] / 2

    if end == 1:
        break
    else:
        count += 1

print(count)

