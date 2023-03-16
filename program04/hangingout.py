print("limit 1-200,cases 0-100: ")
L,X = map(int,input().split()) # using to optimize code and make easier, not covered in class but mentioned in links
current = 0
p = 0
for a in range(X):
    action,b = input().split()
    b = int(b)
    if action[0]=="e":
        if current + b > L:
            p += 1
        else:
            current+=b
    else:
        current-=b
print(p)
