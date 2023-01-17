n,k = map(int, input().split())
lst = list(map(int, input().split()))
sort_lst = sorted(lst)
print(sort_lst[n-k])
