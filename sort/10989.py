n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
    
for i in range(n-1):
    min = lst[i]
    if(min>lst[i+1]):
        temp = min
        min = lst[i+1]
        lst[i+1]=min

for i in range(n):
    print(lst[i])
