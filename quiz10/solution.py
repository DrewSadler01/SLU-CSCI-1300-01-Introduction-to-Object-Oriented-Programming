## kaitlyn.ashabranner@slu.edu, helen.richards@slu.edu, drew.sadler@slu.edu

count=0
while count < 20:
    b=input("Enter a word: ")
    count+=int(b.count(''))
    count=count-1
print(" you have entered "+ str(count) +" characters")
