q=[int(x) for x in input().split(' ')]
N=q[0]
M=q[1]
q=[]
for i in range(M):
    q.append([int(x) for x in input().split(' ')])

print(N,M)
print(q)