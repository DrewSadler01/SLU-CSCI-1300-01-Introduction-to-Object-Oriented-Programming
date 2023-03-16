a=input("Start entering words: ")
b=[]
while a not in b:
    b.append(a)
    a=input()
print("You already entered " + a)
print("You listed", len(b), "distinct words")
