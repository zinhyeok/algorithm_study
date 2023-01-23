import sys
from collections import Counter
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

def get_mode(num):
    if(len(num)==1):
        return num[0]
    cnt = Counter(num).most_common()
    #most_conter 내림차순으로 가져옴
    if cnt[0][1] != cnt[1][1]:
        return cnt[0][0]
    else:
        array = []
        for t in cnt:
            if t[1] == cnt[0][1]:
                array.append(t[0])
        return sorted(array)[1]



avg = round((sum(lst)/n))
mid = lst[n//2]
mode = get_mode(lst)
diff = lst[-1] - lst[0]

print(avg)
print(mid)
print(mode)
print(diff)
