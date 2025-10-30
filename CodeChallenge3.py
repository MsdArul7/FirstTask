def elementRemoval(N, K, A):
    result = -404
    count ={}
    for num in A:
        count[num] = count.get(num,0)+1
    removals = 0
    for count in count.values():
        values = count % K
        if values != 0:
            removals += values
    result = removals        
    return result
N = int(input())
K = int(input())
temp = input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))
print(elementRemoval(N,K,A))