def suming(N):
    return sum([int(a) for a in N]) #Sake of simplicty to get sums

print("Input N 1-100,000, use 0 to end:")
while(True):
    N = input()
    if N == "0":
        break
    big = suming(N)
    p = 11
    while(suming(str(p*int(N))) != big): # p*N
        p = p + 1
        
    print("Output: ")
    print(p)
