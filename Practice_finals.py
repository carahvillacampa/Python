#This page is random code from practice problems:
#Directions:
'''
1. write down instructions
2. test early
3. think it out
4. write pseudocode
'''

#Problem 1
'''
Write function vowel count()
that takes string as input
counts and PRINTS the number of ccurences of vowels only in a string

PC:

1. write funtion
2. use a loop to evaluate each character
3. if vowel store in a string
4. use format string to print it out the ff:
    sample:
    vowelCount('Le tour de France')
    a,e,i,o and u appear respecively 1,3,0,1,1 times.
5. make sure that it's not case sensitive

'''

def vowelCount(string):

    lower_str=string.lower()
    a= 0
    e= 0
    i= 0
    o= 0
    u= 0

    for letter in lower_str:
        if letter == 'a':
            a += len(letter)
        elif letter == 'e':
            e += len(letter)
        elif letter == 'i':
            i += len(letter)
        elif letter == 'o':
            o += len(letter)
        elif letter == 'u':
            u += len(letter)

#Problem 2
'''
Directions:
- function censor () takes the name of a file (a string) as input
- function should open file, read it and write into it
- every occurence of a 4 letter word should be replaced by xxxx
- this function produces no output but it does create file censored.txt in the
current folder

PC:
1. opens two files:
    - one to read the current file
    - one to write the modified file
2. should evaluate each word in string
3. do this by splitting the string
4. evaluate the length of each word
5. if it's equal to 4 then save it to a censored output replaced by xxxx
6. write this output variable to the censored_file

testing2.txt
censored_file.txt
'''

def censor():
    infile= open('/Users/carahvillacampa/Downloads/testing2.txt','r')
    readfile= infile.read()

    splitfile= readfile.split()
    read=readfile

    for word in splitfile:
        if len(word) == 4:
            read= read.replace(word,'xxxx')

    infile1=open('/Users/carahvillacampa/Downloads/censored_file.txt','w')
    writefile= infile1.write(read)
    infile1.close()
    infile.close()
# Problem 3
'''
Make a class
Given string values for the sender, recipient and subject of an email,
write a string format expression that uses variables sender, recipient and
subject that prints as shown here:
'''
class Email:
    def __init__(self):
        self.sender= input('sender email: ')
        self.recipient= input('recipient email: ')
        self.subject= input('purpose of email: ')
    def __repr__(self):
        return 'From: {}\nTo: {}\nSubject: {}'.format(self.sender,
         self.recipient, self.subject)
    def __str__(self):
        return 'From: {}\nTo: {}\nSubject: {}'.format(self.sender,
         self.recipient, self.subject)

#Problem 4  
'''
-add method distance to a class Point
- it takes another Pont object as input and returns the distance to that point
(from the point invoking the method)
Distance formula= sqrt{(x2-x1)**2 + (y2-y1)**2}
'''
import math

class Point():

    def setx(self, x):
        self.x= x
    def sety(self, y):
        self.y= y
    def distance(self,d): #d is just the placeholder for the instance to be passed
        return math.sqrt(((self.x-d.x)**2)+ ((self.y- d.y)**2))
        #d represents the instance 

'''
-Implement a class Vector that supports the same methods as the class
Point.
Vector shouuld support vector addition and product operations
'''

class Vector:
    def __init__(self,x,y):
        self.x= x
        self.y= y  
    def __add__(self,v):
        return '({},{})'.format(self.x + v.x, self.y+ v.y)
    def __sub__(self,v):
        return '({},{})'.format(self.x - v.x, self.y- v.y)
    def __mul__(self,v):
        return '({},{})'.format(self.x * v.x,self.y * v.y)

v1=Vector(2,3)
v2=Vector(3,2)

'''
add to class Animal methods setAge() and getAge() to set and retrieve
the age of the Animal object

''' 
class Animal:

    def setAnimal(self, age, species):
        self.age= age
        self.species= species
    def getAge(self):
        return self.age
    def getSpecies(self):
        return self.species
    def __repr__(self):
        return 'This is a species of the family: {}, and he/she is {} years old'.format(self.species, self.age)
animal=Animal()
animal.setAnimal(34,'cat')

'''
add to class Point methods up(), down(), left() and right()
that move the object one unit in the appropriate direction

'''

class Move(Point):
    
    def up(self):
        return'({},{})'.format(self.x,self.y+1)
    def down(self):
        return'({},{})'.format(self.x-1,self.y)
    def left(self):
        return'({},{})'.format(self.x-1,self.y)
    def right(self):
        return'({},{})'.format(self.x+1,self.y)
           
coor1= Move()
coor1.setx(3)
coor1.sety(4)

'''
2 parts in the final exam:
written exam and final:
coding part is based off homework questions

-Write a short answer.. code snippets
-Errors: logical errors and other types of error
-create a basic constructor
-overload operator
-recreate the bank account stuff
bogus ass proffessor; I can't wait to finish this stupid class
so I won't have to deal with this stupid professor again. bogus
bullshit ass motherfucker
'''
def dict_1():
    Dict1= {'Tyrone':98,'Martha':99,'Claus':87}
    outstanding=[]
    for key in Dict1:
        if Dict1[key] > 90:
            outstanding.append(key)
    return outstanding
'''
Function xmult() that takes 2 integers as input
-returns a list containing all products of integers from the
first list with integers from the second list
'''

def xmult(l1,l2):
    product=[]
    for nums in l1:
        for nums1 in l2:
            product.append(nums*nums1)
    print(product)

def twodi():
    list1=[[2,3,4],[5,6,7],[8,9,7]]

    for row in list1:
        for number in row:
               print(number)

'''
Write a function add2D() that takes two dimensional lists
of the same size as input arguments and increments every
entry in the first list with the value of the corresponding
entry in the second list
'''
def add2D(l1,l2):
    addnum=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            l1[i][j]+=l2[i][j] 
    for row in l1:
        print(row)
def conseq():
    xs = [5, 2, 3, 4, 5]

    for i in range(len(xs)-1):
        print(xs[i+1], end=' ')


'''
In the loop's body, you're indexing not only a[i],
but also a[i+1]. This is also a place for a potential error.
If your list contains 5 items and you're iterating over it
like I've shown in the point 1, you'll get an IndexError.
Why? Because range(5) is essentially 0 1 2 3 4, so when the
loop reaches 4, you will attempt to get the a[5] item.
Since indexing in Python starts with 0 and your list
contains 5 items, the last item would have an index 4,
so getting the a[5] would mean getting the sixth element
which does not exist.
'''

def doubles(l1):
    doubles_list=[]

    for i in range(len(l1)-1):
        if l1[i]*2 == l1[i+1]:
            doubles_list.append(l1[i])
    return doubles_list
'''
Write a function intersect() that takes two lists and returns
True if there is an item that is common to both lists and
False otherwise
'''
    
def intersect(l1,l2):
    
    for nums in l1:
        for nums1 in l2:
            if nums== nums1:
                return True
            return False
'''
Implement function four_letter() that takes as input a list of
words and returns the sublist of all four letter words in the
list
'''
def four_letter(words):
    newlist=[]

    for word in words:
        if len(word)==4:
            newlist.append(word)
    return newlist
'''
Implement function leap() that takes one input argument and
returns True if the year is a leap year and False otherwise.
(A year is a leap year if it is divisible by 4 but not by 100
unless it is divisible by 400, in which case it is a leap year
For example 1700,1800 and 1900 are notleap years but 1600 and 2000
are
'''
def leap(year):

    if year %4==0 and year %400 ==0:
        return True
    else:
        return False
'''
Implement a function mystery() that takes input a positive
integer n and answers this question: How many times can n be
halved(using integer division) before reaching 1? This value
should be returned.
'''
def mystery(n):
    num=[]
    if n == 1:
        return num
    else:
        num.append(n)
        mystery(n//2)
    print(num)
'''
Introduction to Recursion
'''

def countdown(n):
    if n == 0:
        print('Blast the fuck off')
    else:
        print(n)
        return countdown((n-1))

def vertical(n):
    newnum= 0
    if n < 10:
        print(n)
    else:
        vertical(n//10)
        print(n%10)

def vowels(string):
    indx=''
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            indx= i
    print(indx)

'''
Implement the function pixels that takes as input a two dimen
sional list and returns the number of entries that are positive.
It should work on two dimensional list of any size.
'''
def pixels(l1):
    list1=[]
    for group in l1:
        for nums in group:
            if abs(nums) > 0:
                list1.append(nums)
    print(len(list1))

'''
function reverse() that takes input a dictionary( phonebook with names as it's
keys to phonenumbers (values). Function should return another dictionary
representing the reverse phone book mapping phone numbers to the names
'''
def reverse():
    dict1={'T. biggums':6772,'R. restrain':9889,'M. Jackson':9887}

    values={}
    for keys in dict1:
        values[dict1[keys]]= keys
    print(values)
'''
Write a function ticker() that takes a string (name of file as input)
File will contan company names and stock (ticker) symbols. In this file,
a company name will occupy a line and it's stock symbol will be on the next
line. Following this line will be a line with another company name and so on.
Your program will read the file and store the name and stock symbol in a
dictionary.
Then it will provide an interface to the user so that the
user can obtain the stock symbol for a given comapny.
Test your code on the NASDAQ
100 list of stock given in file NASDAQ.txt
'''

def ticker():
    infile= open('/Users/carahvillacampa/Downloads/text.txt','r')
    readfile= infile.read()
    infile.close()

    splitfile= readfile.split()
    value={}

    for i in range(len(splitfile)-1):
        if i %2==0:
            value[splitfile[i]]=splitfile
    print(value)
'''
Implement function names() that takes no input and repeatedly asks the user to
enter the first name of a student in a class. When the user enters the empty
string, the function should print for every name the students with that name

Pc:

1. Idea: use a wile loop to repeatedly ask names
2. Use userinput
3. If empty string:
it should return the values that was stored in the dictionary
'''

def names():
    lst1= []

    dct={}
    while True:
        name= input('Enter name: ')
        lst1.append(name)
        if name ==' ':
            for names in lst1:
                if names in dct:
                    dct[names] +=1
                else:
                    dct[names]=1
            for keys in dct:
                value=dct[keys]
                key= keys
                result='people with the name {}: {}'.format(value, key)
                return result
'''
-Develop a single game that teaches kindergartners how to add single numbers
your function game will take an integer n as input and then ask n single-digit
addition questions. The numbers to be added should be chosen randomly from
range [0,9]. The user will enter the answer when prompted. Your function
should print 'Correct' for the correct answers and 'Incorrect' for the incorrect
answers. After n questions, your function should print the number of correct
answers.

PC:

-generate random integers using the random module
-add integers and evaluate if true

'''
import random

def game(n):
    
        correct_answer= 0 #always put the accumulator out the loop
        incorrect_answer=0 #otherwise, it's gonna print individual
                           # results and not show the total results
    
        for i in range (n+1):
            random_1= random.randrange(0,10)
            random_2= random.randrange(0,10)
            eq= random_1+random_2

            print(str(random_1)+ '+' +str(random_2))
            answer= int(input('Enter answer: '))

            
            if answer == eq:
                correct_answer += 1
            else:
                incorrect_answer += 1
    
        print('incorrect answers: {}'.format(incorrect_answer))
        print('correct answers: {}'.format(correct_answer))

'''
Add to class Animal methods setAge() and getAge() to set and
retrieve the age of the Animal object
'''
class Animal: 
    def setAge(self,age):
        self.age= age
    def getAge(self):
        return self.age
'''
Add a constructor to class REctangle so that the length and width of
the rectangle can be set at the time the Rectangle object is
created. Use default values of 1 if the length ow width is
not specified
'''

class Rectangle:
    def __init__(self, xcoord=1, ycoord=1):
        self.x= xcoord
        self.y= ycoord
    def perimeter(self):
        return 2*(self.x+self.y)
    def area(self):
        return self.x*self.y

'''
implement your own string class myStr that behaves like class
str except that:
- addition should return the sum of two strings
(instead of concantenation)
- multiplication should return the product of the lengths
of two strings
'''

class MyStr:
    def __init__(self,string):
        self.string=string
    def __add__(self,other):
        value= self.string + other.string
        return 'Add the strings: {}'.format(len(value))
    def __mul__(self,other):
        prod= len(self.string) * len(other.string)
        return 'The product is: {}'.format(prod)

        
'''
develop a class called Bankaccont() that supports these methods:
__init__() initializes the bank account balance to the value
of the input argument.
__withdraw__() takes an amount as input and withdraws it from
the balance
deposit() takes an amount as input and adds it to the balance
balance() returns the balance on the account
'''

class Bankaccount:
    def __init__(self, bal):
        self.bal= bal
    def deposit(self, depo):
        self.depo= depo
        self.bal += self.depo
        return self.bal
    def withdraw(self,amnt):
        self.amount=amnt
        wthdrw= self.bal-self.amount
        return wthdrw


#Practice Section 1
#Exercises: OOP, Dictionaries, loops

'''
Exercise 1:
Implement a clss myINt that behaves almost the same as the class
int. Except when trying to add an object of my typeINT. it
returns the length of the string passed Then this
strange behavior occurs
'''
class MyINT:
    def __init__(self, string):
        self.string= string
    def __add__(self,other):
        add_val= self.string + other.string
        return len(add_val)

'''
Exercise 2:
Implement function easy crypto() that tajes as input a string and
prints its encryption defined as follows:

Every character at an odd position i in the alphabet will be
encrypted with the character i+1, and every chcarcter at an even
position i will be encrypted with the character at i-1. In other
words, a is encrypted with 'b' and so on.
It shouldn't be case sensitive
'''

#find() finds the index of the letters
def crypto(string):
    string= string.lower()
    alpha= 'abcdefghijklmnopqrstuvwxyz'

    for letters in string:
        num=alpha.find(letters)
        if num % 2==0:
            print(alpha[num+1], end=' ')
        else:
            print(alpha[num-1], end=' ')

'''
Exercise 3:
Implement function test() that takes input one integer and prints
'Negative', 'Zero' or 'Positive depending on its value
'''

def test(n):

    if n < 0:
        print('Negative')
    elif n ==0:
        print('Zero')
    else:
        print('Positive')

#Problem: OOP

'''
implement class worker that supports these methods:
1. __init__() that takes as input the worker's name and the
hourly pay rate( as number
2. changeRate() takes the new pay rate as input and changes
the workers pay rate to the new hourly rate
3. Pay(): takes the number of hours worked as input and prints
'Not implemented'
'''


class Worker:
    def __init__(self, name, pay_rate):
        self.name= name
        self.pay= pay_rate
    def changeRate(self, new_rate):
        self.pay= new_rate
        return self.pay
    def pay_r(self, hours1):
        self.hours1= hours1
        hour_pay= self.hours1 * self.pay
        return hour_pay

#Practice Section 2
#Exercises: While loop, For loop, Files

'''
Exercise 1:
Implement function indexes() that takes input a string and a one
leter character and returns a [list] of indexes at which the letter
occurs in the word

Eg: indexes('misisipi','s')
[2,3,5,6]
'''

def indexes(string, letter):
    l1=[ ]
        
    for i in range(len(string)):
        if letter == string[i]:
            l1.append(i)
    return l1
      
indexes('mississipi','s')

'''
Exercise 2:

Implement a function that asks the user to enter the name of his/her
fav city and it keeps iterating. When the user enters an empty string
it stops and returns a list of the iterated cities
'''

def favorite():

    cities= []

    while True:
        fav= input('Enter favorite city: ')

        if fav != ' ':
            cities.append(fav)
        else:
            return 'This is a list of the cities entered: {}'.format(cities)


'''
Exercise 3:

The cryptography of the function crypt() that takes input the name of a
file in the current directory and every occurence of a 5 word letter
should convert it to: xxxxx

and the contents should be returned to another file called
secret_file
'''

def crypt():
    infile= open('/Users/carahvillacampa/Downloads/testing2.txt','r')
    readfile1= infile.read()
    infile.close()

    splitfile= readfile1.split()

    for words in splitfile:
        if len(words) == 5:
            readfile1 = readfile1.replace(words,'xxxxx')
    print(readfile1)
    

#Problem: Dictionary

'''
Implement function names() that takes no input and repeatedly asks
the user to enter the first name of a student in a class. When the
user enters the empty string, the function should print for every
name the number of students with that name
'''

def names1():

    names_1=[ ]

    count= {}
    while True:
        name= input('Enter a name: ')

        if name !=' ':
            names_1.append(name)

        else:
            name ==' '
            for names  in names_1:
                if names in count:
                    count[names] += 1
                else:
                    count[names]=1
            return 'The names and numbers are as follows: {}'.format(count)
#Practice Section 3
#Exercises: sets, tuples, for loop

'''
Exercise 1:

Using a loop counter patern, construct sets mult3,
mult5 and mult7 of
non negative multiples of 3,5,7 respectively less
than 100. Then using these
three sets, write expressions that
return multiples of 3,5,35,105
'''
def setPatterns():
    set1={3,5,7}

    val3=set()
    val5=set()
    val7=set()

    
    for num in set1:
        for i in range(30):
            if num == 3:
                val3.add(num*i)
            elif num == 5:
                val5.add(num*i)
            else:
                num ==7
                val7.add(num*i)
    
    print(val3.intersection(val5))
    print(val3.intersection(val7))
    print(val5.intersection(val7))
        
        
       
print(setPatterns())


'''
Exercise 2:
-open the file class_roster.txt
-creates a dictionary that separates firstname: lastname
, schoolyear and student ID
should format:

Firstname:
Lastname:
School year:
-returns a dictionary of the above
'''


'''
Exercise 3:

Write a function inBoth() that takes two lists and returns True if there is an
item that is common to both lists and False otherwise
'''

#Problem: Recursion (fully understand it)
                
        
'''
Implement recursive method reverse() that takes on negative integers as input
and prints its digits vertically, starting with the low-order digit

Eg: reverse(3124)
4
2
1
3
'''














