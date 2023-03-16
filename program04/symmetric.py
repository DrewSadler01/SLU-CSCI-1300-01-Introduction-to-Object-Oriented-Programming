count = 1
while True:
    print("Enter # of names: ")
    number = int(input())
    if number == 0:
        break
    
    print("Enter "+str(number)+" names: ")
    names = [input() for a in range(number)] #used to clean up code a bit
    print ("SET",count)
    for b in range(0, number, 2):  #special case for number of names
        print(names[b])
        
    for b in range(number-(number%2)-1,-1,-2): #changing the positions/values of range
        print(names[b])
        
    count += 1
