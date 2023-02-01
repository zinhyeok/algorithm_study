N = int(input())

devil_Num = 666
count = 0

while True:
    if "666" in str(devil_Num):
        count += 1
    if count == N:
        break
    devil_Num += 1

print(devil_Num)