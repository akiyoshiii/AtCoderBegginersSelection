A = int(input()) #500
B = int(input()) #100
C = int(input()) #50
X = int(input()) #合計
count = 0 #うまくいったパターン数

for a in range(A + 1):
    for b in range(B + 1):
        for c in range (C + 1):
            sum = 500 * a + 100 * b + 50 * c
            if sum == X:
                count += 1

print(count)