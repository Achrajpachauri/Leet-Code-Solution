n = 9
time = 4
count = 1

if time <=n:
    return n

for i in range(1,time+1):
    
    if count==n+1:
        count=1
    print(count,end=" ")
    count+=1

print(n-count)