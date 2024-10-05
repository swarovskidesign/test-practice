mx = -1
s = 0
count = 0
for i in range(1, 11):
    x = int(input())
    if x <= -1:
        s += x
        count += 1
        if mx < x:
            mx = x
            
if count == 0:
    print("NO")  
else:
    print(s)
    print(mx)