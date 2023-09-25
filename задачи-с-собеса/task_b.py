# N=input()
# b=input()
check=3

if check==1:
    N=5
    b='-1 -1 -1 -1 -1'
if check==2:
    N=5
    b='1 3 -1 1 0'
if check==3:
    N=5
    b='1 3 4 2 -1'
    
b=[int(x) for x in b.split(' ')]

# def task_b(b):
#     if b[0]==-1:
#         return 'NO'
#     for i in range(len(b)):
#         if b[i]!=-1 or b[i]!=-2:
#             q=b[i]
#             b[i]=-2


#             return 'YES'
#     b=set(b)
#     if len(b)<=2:
#         return 'NO'
# ans=task_b(b)

# ans='NO'
# i=0
# if N==1:
#     ans='NO'
# else:
#     while set(b)!={-2,-1}:
#         q=b[i]
#         if i==0 and q==-1:
#             ans='NO'
#             break
#         if q==-2:
#             ans='YES'
#             break
#         if q!=-1 and q!=-2:
#             print(b)
#             b[i]=-2
#             t=0
#             while t==0:
#                 print(b)
#                 q2=b[q]
#                 b[q]=-2
#                 if q2==-1:
#                     t=1
#                 if q2==-2:
#                     ans='YES'
#                     t=100
#             if t==100:
#                 ans='YES'
#                 break
#         i+=1
# print(ans)

ender=False
ans='NO'
i=0
while ender==False:
    if b[i]==-1:
        ender=True
    if b[i]==-2:
        ans='YES'
        ender=True
    if b[i]!=-1 and b[i]!=-2:
        t=i
        i=b[i]
        b[t]=-2
    # print(f"{b}")
    

print(ans)