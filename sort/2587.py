lst = []
for i in range(5):
    lst.append(int(input()))
lst.sort()

avg = int(sum(lst)/len(lst))
mid = lst[2]

print(avg)
print(mid)
