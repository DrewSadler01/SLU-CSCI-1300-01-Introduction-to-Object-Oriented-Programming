# -*- coding: utf-8 -*-
"""Copy of Exam02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zEOZmdzRyV7nI5cIcH0xZDHR7yfz6bmQ

# Exam Instructions


1.   Read these instructions carefully
2.   Make a copy of this document:

     `File->Save a copy in Drive...`
3.   Complete the exam by placing your answers in the space provided. ONLY use the space provided. 
4.   Download your solution as a Python file:

    `Download .py`
5.   Submit the downloaded file to your git repository under `exam02` directory.

Please note that for questions that involve executable code, you may run your code directly on this site by clicking the "play" button in the top left corner of the code. However, not all questions involve complete code and this site will not support cs1graphics. You are allowed to test using Python on your own computer, but please make sure that your answers are properly transcribed to this exam.

# Academic Integrity

While you are free to reference the book, notes from this class, or general Python references, you may not seek any direct or indirect help to answer the specific exam questions, nor are you to communicate with anyone else regarding the exam.  All answers most be entirely your own work.

Any violation of the Academic Integrity policy will result in the grade of zero for this exam. Additionally, anyone caught violating the Academic Integrity policy will be prohibited from taking the final exam in this course.

Please sign your name in the box below to confirm that all answers are your own.
"""

# I have abided by the policy on Academic Integrity
# and all answers given below are my own.
#
# [insert your name here]

"""# Question 1 (15 points)

Give Python code that expresses the following flow of control, presuming the use of A, B, C as
boolean expressions and V, W, X, Y, Z as executable statements.
Your code should express this logic using each of the above characters once and only once.

![alt text](data:image/png;base64,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)

We will get you started. Please comlete the code below.
"""

# Your answer here
if A:
  if C:
    x
  else:
    W
  Y
else B:
  V
Z

"""# Question 2 (15 points)

Assume that identifier `movies` references a list of strings which are titles of all movies from the Internet Movie Database. Give a segment of code that prints the title of a movie that possesses the ***greatest number of words*** in the title (where we assume whitespace is what separates words). In case of a tie, printing any such example will suffice.

For example, with

    movies = ['The Shawshank Redemption',
              'The Godfather',
              'The Godfather: Part II']

your code should print

    The Godfather: Part II

as that title is considered to have four words.
"""

# Your answer here
# I made movies a value cause I wasn't sure if it's tested on just those values.
movies =['The Shawshank Redemption','The Godfather','The Godfather: Part II']
spaces = 0
for a in range(len(movies)):
    if movies[a].count(' ') > spaces:
        spaces = movies[a].count(' ')
        temp = a
print(movies[temp])

"""# Question 3 (15 points)

The function `random( )` returns a randomly chosen floating point value between `0.0` and `1.0`. Write a program that repeatedly calls the `random( )` function, stopping only when it receives a value that differs from a previously drawn value by at most `0.05`. Your program should print the total number of calls that were made.

For example, if the random number generator produced the sequence `0.54 0.37, 0.91, 0.74, 0.60, 0.41, ...` it would stop because `0.41` differs from previous `0.37` by at most `0.05`, and it would output that a total of `6` calls were made.
"""

# Your answer here
from random import random
numbers=[]
rand=0
check=0
while(check!=1):
    rand=random()
    numbers.insert(len(numbers),rand)
    if len(numbers) >=2: #has to have more than 1 value
        for a in range(len(numbers)):
            if((numbers[a-1]-numbers[a])<=.05) and ((numbers[a-1]-numbers[a])>=-.05):
                check=1
print('Took '+ str(len(numbers))+' tries.')

"""# Question 4 (15 points)

On the classic gameshow *The Price Is Right*, contestants must guess the price of an object (guesses are distinct). The winner is determined to be the person whose bid is closest to the correct price, but without going over. For example, if the guesses were
```
Alice  430
Bob    538
Carol  487
David  550
```
and the true price were `520`, then Carol has the winning bid with `487`. With the same bids as above, if the actual price had been `420`, then no one would win, as everyone bid too high.

Your job is to implement a function with signature `judge(auction, price)` in which `auction` is a nonempty list of (person, guess) tuples and `price` is the actual price. The function must return the name of the winning person (or `None`, if no one wins). 

For example, the first scenario above might be expressed as
``` 
judge( [('Alice', 430), ('Bob', 538), ('Carol', 487), ('David', 550)], 520)
```
and the string `'Carol'` should be returned as the winner.

**Your function may assume that all parameters are valid.**
"""

# Your answer here
def judge(auction, price):
# Auction consist of (name, guess) and price is just an int
    WinName="None"
    check=0
    WinBrack=[]
    for a in range(len(auction)):
        if(auction[a][1]<=price):
            WinBrack = WinBrack + auction
            if(WinBrack[a][1]>check):
                WinName=WinBrack[a][0]
                check=WinBrack[a][1]
    return WinName

"""# Question 5 (15 points)

The preceding problem involved a function with signature `judge(auction, price)` in which auction was assumed to be a list of (**str**,**int**) tuples, and `price` a positive integer. We require that `auction` be nonempty, that names be nonempty strings, and that the integer guesses be positive and *distinct*. An example of valid parameters is
```
judge( [('Alice', 430), ('Bob', 538), ('Carol', 487), ('David', 550)], 520)
```

Give the initial portion of the function body that performs **strict error-checking** of all parameter requirements, raising appropriate `Error` instances as necessary.

(You do not need to repeat your implementation of the logic of the function from the preceding question, just the error checking.)
"""

# Your answer here

def judge(auction, price):
    for a in range(len(auction)):
        if type(auction[a]) != tuple:
            raise TypeError("Auction should consist of a name and price")
        if type(price) != int:
            raise TypeError("Price has to be an integer")
        if (price <=0):
            raise ValueError("The price cannot be 0 or a negative")
        if type(auction[a][0]) != str:
            raise TypeError("Each contestants name should be a string")
        if ((auction[a][0]) == "") or ((auction[a][0]) == " "):
            raise ValueError("Every contestant needs a name")
        if type(auction[a][1]) != int:
            raise TypeError("Price guesses have to be a integer")
        if auction[a][1] <= 0:
            raise ValueError("Price guesses cannot be 0 or negative")
        if auction[a-1][1] == auction[a][1]:
            raise ValueError("You cannot have 2 matching guesses")

"""# Question 6 (25 points)

Implement a function with signature `barGraph(w, h, data)` which creates and returns a `cs1graphics.Canvas` instance that has width `w` and height `h` and which visualizes the given `data` as a bar graph. The data will be a nonempty list of positive integers. (You do not need to error-check the parameters.)

Your visualization must have rectanglar bars with equal width that collectively use 80% of the width of the canvas (leaving 10% padding on left and right) and the bars should be vertically aligned at their bottom edge such that the maximum value in the data results in a bar that uses 80% of the height of the canvas (leaving 10% padding at top and bottom).

As an example, the call `barGraph(400, 300, [5, 8, 2, 7])` should produce the following image:

![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZIAAAEuCAYAAACkipT0AAAAAXNSR0IArs4c6QAADvNJREFUeAHt2TFuVUcYhuFDcAEFhUFCoqTxBi6FO0TBHtxQWmIJ3giVSxokt3TQWHLh5iLcugFBRWMXXkASIzjVJBofZ5xvxg9SlJthrs9/nj/Rq4hp8osAAQIECFxD4M6v7/55jZ/hqwQIECBwewXubPx+983NzWm1Wv3+R38nQIAAAQL/KLBer6fz8/Ofvz+H5DIiHz58+Mcv+Q0CBAgQIPBb4OXLl9PHjx9//uMfvw/9nQABAgQILBEQkiVqvkOAAAECs4CQzBQ+ECBAgMASASFZouY7BAgQIDALCMlM4QMBAgQILBEQkiVqvkOAAAECs4CQzBQ+ECBAgMASASFZouY7BAgQIDALCMlM4QMBAgQILBEQkiVqvkOAAAECs4CQzBQ+ECBAgMASASFZouY7BAgQIDALCMlM4QMBAgQILBEQkiVqvkOAAAECs4CQzBQ+ECBAgMASASFZouY7BAgQIDALCMlM4QMBAgQILBEQkiVqvkOAAAECs4CQzBQ+ECBAgMASASFZouY7BAgQIDALCMlM4QMBAgQILBEQkiVqvkOAAAECs4CQzBQ+ECBAgMASASFZouY7BAgQIDALCMlM4QMBAgQILBEQkiVqvkOAAAECs8DG/MmHIQXevXs3HR8fD/luN/VSr169mlar1U09znMIdCcgJN2t7GoDX0bk6Oho2trautoX3f4pcHp6Ot27d09I/PtA4F8EhORfcEb5rcuI7O7ujvI6N/oe+/v7N/o8DyPQo4A/I+lxa2YmQIBAkICQBC3DKAQIEOhRQEh63JqZCRAgECQgJEHLMAoBAgR6FBCSHrdmZgIECAQJCEnQMoxCgACBHgWEpMetmZkAAQJBAkIStAyjECBAoEcBIelxa2YmQIBAkICQBC3DKAQIEOhRQEh63JqZCRAgECQgJEHLMAoBAgR6FBCSHrdmZgIECAQJCEnQMoxCgACBHgWEpMetmZkAAQJBAkIStAyjECBAoEcBIelxa2YmQIBAkICQBC3DKAQIEOhRQEh63JqZCRAgECQgJEHLMAoBAgR6FBCSHrdmZgIECAQJCEnQMoxCgACBHgWEpMetmZkAAQJBAkIStAyjECBAoEcBIelxa2YmQIBAkICQBC3DKAQIEOhRQEh63JqZCRAgECSwETSLUQgQGExgvV5Pb9++HeytbvZ1tre3p52dnZt96BWfJiRXBHOdAIF6gYODg+no6Gja2tqq/5Kbs8DFxcX0+fNnIZlFfCBA4FYKXEZkd3f3Vr77dV/68v/o3r9/f90f0/z7/oykObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsASEZe7/ejgABAs0FhKQ5sQcQIEBgbAEhGXu/3o4AAQLNBYSkObEHECBAYGwBIRl7v96OAAECzQWEpDmxBxAgQGBsgY301zs4OJjW63X6mLHznZycTE+ePImdz2AECPQvEB+SN2/eTA8ePPj5V//cN/8GP378EJKbZ/dEArdKID4kl9t4/vz5tFqtbtVi/quX3dvb+69+lJ9DgACBooA/IymyOCRAgACBWgEhqZVyjwABAgSKAkJSZHFIgAABArUCQlIr5R4BAgQIFAWEpMjikAABAgRqBYSkVso9AgQIECgKCEmRxSEBAgQI1AoISa2UewQIECBQFBCSIotDAgQIEKgVEJJaKfcIECBAoCggJEUWhwQIECBQKyAktVLuESBAgEBRQEiKLA4JECBAoFZASGql3CNAgACBooCQFFkcEiBAgECtgJDUSrlHgAABAkUBISmyOCRAgACBWgEhqZVyjwABAgSKAkJSZHFIgAABArUCQlIr5R4BAgQIFAWEpMjikAABAgRqBYSkVso9AgQIECgKCEmRxSEBAgQI1AoISa2UewQIECBQFBCSIotDAgQIEKgVEJJaKfcIECBAoCggJEUWhwQIECBQKyAktVLuESBAgEBRQEiKLA4JECBAoFZASGql3CNAgACBooCQFFkcEiBAgECtgJDUSrlHgAABAkUBISmyOCRAgACBWgEhqZVyjwABAgSKAkJSZHFIgAABArUCQlIr5R4BAgQIFAWEpMjikAABAgRqBYSkVso9AgQIECgKCEmRxSEBAgQI1AoISa2UewQIECBQFBCSIotDAgQIEKgVEJJaKfcIECBAoCggJEUWhwQIECBQKyAktVLuESBAgEBRQEiKLA4JECBAoFZASGql3CNAgACBooCQFFkcEiBAgECtgJDUSrlHgAABAkUBISmyOCRAgACBWgEhqZVyjwABAgSKAkJSZHFIgAABArUCQlIr5R4BAgQIFAWEpMjikAABAgRqBYSkVso9AgQIECgKCEmRxSEBAgQI1AoISa2UewQIECBQFBCSIotDAgQIEKgVEJJaKfcIECBAoCggJEUWhwQIECBQKyAktVLuESBAgEBRQEiKLA4JECBAoFZASGql3CNAgACBooCQFFkcEiBAgECtgJDUSrlHgAABAkUBISmyOCRAgACBWgEhqZVyjwABAgSKAkJSZHFIgAABArUCQlIr5R4BAgQIFAWEpMjikAABAgRqBYSkVso9AgQIECgKCEmRxSEBAgQI1AoISa2UewQIECBQFBCSIotDAgQIEKgVEJJaKfcIECBAoCggJEUWhwQIECBQKyAktVLuESBAgEBRQEiKLA4JECBAoFZASGql3CNAgACBooCQFFkcEiBAgECtgJDUSrlHgAABAkUBISmyOCRAgACBWgEhqZVyjwABAgSKAkJSZHFIgAABArUCQlIr5R4BAgQIFAWEpMjikAABAgRqBYSkVso9AgQIECgKCEmRxSEBAgQI1Aps1F50j8BtFDg7O5u+fPky7e3t3cbXv/Y7Hx4eTk+fPr32z/EDsgWEJHs/pvufBb5//z7dv39/+vbt2/88SZ+P//r1q5D0uborTS0kV+Jy+TYKbG1tTbu7u7fx1a/9zicnJ9f+GX5AvoA/I8nfkQkJECAQLSAk0esxHAECBPIFhCR/RyYkQIBAtICQRK/HcAQIEMgXEJL8HZmQAAEC0QJCEr0ewxEgQCBfQEjyd2RCAgQIRAsISfR6DEeAAIF8ASHJ35EJCRAgEC0gJNHrMRwBAgTyBYQkf0cmJECAQLSAkESvx3AECBDIFxCS/B2ZkAABAtECQhK9HsMRIEAgX0BI8ndkQgIECEQLCEn0egxHgACBfAEhyd+RCQkQIBAtICTR6zEcAQIE8gWEJH9HJiRAgEC0gJBEr8dwBAgQyBcQkvwdmZAAAQLRAkISvR7DESBAIF9ASPJ3ZEICBAhECwhJ9HoMR4AAgXwBIcnfkQkJECAQLSAk0esxHAECBPIFhCR/RyYkQIBAtICQRK/HcAQIEMgXEJL8HZmQAAEC0QJCEr0ewxEgQCBfQEjyd2RCAgQIRAsISfR6DEeAAIF8ASHJ35EJCRAgEC0gJNHrMRwBAgTyBYQkf0cmJECAQLSAkESvx3AECBDIFxCS/B2ZkAABAtECQhK9HsMRIEAgX0BI8ndkQgIECEQLCEn0egxHgACBfAEhyd+RCQkQIBAtICTR6zEcAQIE8gWEJH9HJiRAgEC0gJBEr8dwBAgQyBcQkvwdmZAAAQLRAkISvR7DESBAIF9ASPJ3ZEICBAhECwhJ9HoMR4AAgXwBIcnfkQkJECAQLSAk0esxHAECBPIFhCR/RyYkQIBAtICQRK/HcAQIEMgXEJL8HZmQAAEC0QJCEr0ewxEgQCBfQEjyd2RCAgQIRAsISfR6DEeAAIF8ASHJ35EJCRAgEC2wET3dr+EODw+nT58+9TBq3IwXFxfT6enptL+/HzdbDwOdnZ3xu8ai+F0D7++vXv7328Ov+JC8fv16Oj4+7sEycsZnz579nOvhw4eR86UP9eLFi2ljY2Pit2xTl353796dHj16tOwH3PJvPX78eNre3o5XiA/Jzs7OdPmXXwQIECCQKeDPSDL3YioCBAh0IyAk3azKoAQIEMgUEJLMvZiKAAEC3QgISTerMigBAgQyBYQkcy+mIkCAQDcCQtLNqgxKgACBTAEhydyLqQgQINCNgJB0syqDEiBAIFNASDL3YioCBAh0IyAk3azKoAQIEMgUEJLMvZiKAAEC3QgISTerMigBAgQyBYQkcy+mIkCAQDcCQtLNqgxKgACBTAEhydyLqQgQINCNgJB0syqDEiBAIFNASDL3YioCBAh0IyAk3azKoAQIEMgUEJLMvZiKAAEC3QgISTerMigBAgQyBYQkcy+mIkCAQDcCQtLNqgxKgACBTAEhydyLqQgQINCNgJB0syqDEiBAIFNASDL3YioCBAh0IyAk3azKoAQIEMgUuPNrrD83Nzen1WqVOaWpCBAgQCBKYL1eT+fn55cz3ZlDEjWhYQgQIECgF4HfHellXnMSIECAQJrAX+Wvi6MYPxj1AAAAAElFTkSuQmCC)
"""

# Your answer here
from cs1graphics import *
def barGraph(w, h, data):
    canvas=Canvas(w, h)
    length=len(data)
    temp=[]
    height=0
    BotSpace=0
    move=0
    maxH=0
    for a in data:
       temp.append(a)
    temp.sort()
    maxH=temp[-1]
    width=(w/(length+1))   #length+1 account for invis space
    move=width
    for b in data:
        height=((b/maxH)*(h*(8/10)))  #makes max number into % of screen
        BotSpace=((h-(height/2)))-((1/10)*h) #1/10*h space from bottom
        graph=Rectangle(width,height,Point(move,BotSpace)) 
        graph.setFillColor('grey')
        graph.setBorderWidth(1)
        canvas.add(graph)
        move=move+width
    return canvas