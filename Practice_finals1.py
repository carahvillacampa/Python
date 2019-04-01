def dict_1():
    Dict1= {'Tyrone':98,'Martha':99,'Claus':87}

    outstanding=[]

    for key in Dict1:
        if Dict1[key] > 90:
            outstanding.append(key)
    return outstanding


#Section 4 Practice
#Exercises


'''
Write a program which will find all such numbers
which are divisible by
7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a
comma-separated sequence on a single line.

'''

def divi():

    for i in range(2000,3001):
        if i % 7 ==0 and not i % 5==0:
            print('{},'.format(i),end=' ')


'''
With a given integral number n, write a program to generate a
dictionary that contains (i, i*i) such that is an integral number
between 1 and n (both included). and then the program should print
the dictionary.Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
def integral(n):

    dct={}
    for i in range(1,n+1):
        dct[i]=i*i
    print(dct)

'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class Get:
    def __init__(self, string):
        self.string= string
    def getString(self):
        return self.string
    def printString(self):
        return self.string.upper()

#Problems

'''
Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the
program:
100,150,180
The output of the program should be:
18,22,24
'''
import math

def variable(n,n1,n2):
    C= 50
    H=30
    D= [n,n1,n2]

    
    for num in D:
        Q= math.sqrt ((2*C*num)/H)
        print('{},'.format(int(Q)),end=' ')
#Section 5 Practice
#Exercises:

'''
Write a program that accepts a comma separated sequence of words as
input and prints the words in a comma-separated sequence after sorting
them alphabetically.Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''

def sortIT(string):
    
    sortedlst=''
    for words in string:
        sortedlst=sorted(string)
    print(sortedlst)

'''
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a
single line.
Hints:
In case of input data being supplied to the question, it should be assumed
to be a console input.


'''
def evenNum():
    for i in range(100,300+1):
        if i %2 ==0:
            print('{},'.format(i),end=' ')


'''
Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically.Suppose the following input is supplied to
the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

'''
def sortWords(string):
    split= string.split()
    split=sorted(split)

    setwords=set()
    for words in split:
        setwords.add(words)

        
sortWords('hello world and practice makes perfect and hello again')

#Problem

'''
Question:
You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are numbers.
The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
(Tom,19,80),
(John,20,90),
(Jony,17,91),
(Jony,17,93),
(Json,21,85)
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]
Hints:
In case of input data being supplied to the question, it should be assumed
to be a console input.
We use itemgetter to enable multiple sort keys.
'''
from operator import itemgetter, attrgetter



def tup():
    l = []
    while True:
        s = input('Enter name/age/score: ')
        if not s:
            break
        l.append(tuple(s.split(",")))


##from urllib.request import urlopen
##
##response= urlopen('file:///Users/carahvillacampa/Downloads/mars_sample.html')
##html=response.read().decode()
##
##lower=html.lower()

'''
Write methods news() that takes a URL of a news web site and a list of news topics
and computes the number of occurences of each topic in the news
'''
##from urllib.request import urlopen
##def news(url,l1):
##
##    response_1= urlopen(url)
##    html1=response_1.read().decode().lower()
##
##    for words in l1:
##        num_words= html1.count(words)
##        print('{} appears {} times'.format(words,num_words))
##
   
##infile=open('/Users/carahvillacampa/Downloads/mars_sample.html','r')
##readfle=infile.read()
##infile.close
##
##from html.parser import HTMLParser
##
##class LinkParser(HTMLParser):
##    def handle_starttag(self,tag,attrs):
##        if tag== 'a':
##            for attr in attrs:
##                if attr[0] == 'href':
##                    print(attr[1])
##

###all classes inherit from class object
##from urllib.request import urlopen
##def getWeb():
##    response= urlopen('http://condor.depaul.edu/ymendels/243/').read().decode()
##    print(response)

##class LinkParser(HTMLParser):
##    def handle_starttag(self, tag, attrs):
##        print( 'handled tag: {} with {}'.format(tag, attrs))
##    def handle_endtag(self,tag):
##        print('handled tag: {}'.format(tag))

###set the instance with the overidden HTMLParser because the old HTMLParser
###doesn't really do anything.
##def countwords(url):
##    file = urlopen(url)
##    html = file.read().decode()
##
##countwords('http://condor.depaul.edu/ymendels/130/mozart.htm')
##
##        
##class Parser(HTMLParser):
##    def handle_starttag(self, tag, attrs):
##        if tag == 'a':
##            for attr in attrs:
##                if attr[0] == 'href':
##                    print(attr[1])
# parse.feed(html)
# feed is used to connect the html contents of a url opened by your method and
#feeds it to the HTMLParser class that you've over written

#Section 5 Practice
#Exercises: 

#Section 5
#Excercises: Classes x 3
'''
Exercise 1:
- Translate these overloaded operator xpressions
to appropriate method calls
a. x > y __gt__()
b. x != y __ne__()
c. x % y x.__mod__(y)
d. x//y x.__florrdiv__()
e. x or y
'''

'''
Exercise 2:
Develop a class myList that is a subclass of the built-in class. The only
difference between myList and list is that the sort method is overridden.
myList containers should behave just like regular lists, except as shown next:
x= myList([1,2,3])
'''
class List:
    def __init__(self, l1):
        self.list_1= l1
        
class MyList(List):
    def __init__(self, l1):
        super().__init__(l1)
    def reverse(self):
        self.list_1.reverse()
        return self.list_1
'''
Exercise 3:
Question:
Define a function which can generate a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.
The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
'''
#Problem: Classes

'''
Implement the container class Stat that stores a sequence of numbers and provides
statistical information about the numbers. It supports an overload constructor that initializes
the container and the methods shown.

s=Stat()
s.add(23)
s.add(4)

methods:
- min()
- max()
- sum()
- len()
- mean()
- s.clear()
'''
class Stat:
    
    def add(self, number):
        self.lst= [ ]
        if self.lst == [ ]:
            self.lst.append(number)
            
    def getlst(self):
        return self.lst
    def max(self):
        return max(self.lst)
    def min(self):
        return min(self.lst)
    def sum(self):
        counter= 0
        for num in self.lst:
            counter += num
        return counter
##l1= Stat()
##l1.add(3)
##l1.add(4)
##l1.add(7)
##l1.add(80)
##print(l1.getlst())
#section 6 practice

#1
'''
Question:
Write a program which accepts a sequence of comma separated
digit binary numbers as its input and then check whether they
are divisible by 5 or not. The numbers that are divisible by 5
are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
def binary(l1):
    fiv_lst=[ ]
    for num in l1:
        if num % 5 == 0:
            fiv_lst.append(num)
    return fiv_lst
##print(binary([100,11,1010,1001]))

#2
'''
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
def high(sentence):
    letters= [ ]
    numbers= [ ]
    clean_sent= sentence.replace(' ','').lower()
    for char in clean_sent:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            letters.append(char)
        else:
            numbers.append(char)
    return 'Letters {}\nNumbers {}'.format(len(letters),len(numbers))    
##print(high('This is a crazy ass sentence123'))

#3
'''
Question:
Write a program that accepts a sentence and calculate
the numberof upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
#4
def low(sentence):
    clean_sentence= sentence.replace(' ','')
    upper=[ ]
    lower=[ ]
    for char in clean_sentence:
        if char .isupper():
            upper.append(char)
        else:
            lower.append(char)
    return 'Upper {}\n Lower {}'.format(len(upper),len(lower))
##print(low('THE cringiest videos in instagram IS CRAZY'))


#5
'''
Write a python expression according to these statements:

1. the number of characters in the word anachronistically is more than the
number of characters in the word counterintuitive.
2. The word 'misinterpretation' appears earlier in the dictionary than the word
misinterpretation
'''
def evaluate():
    a= 'anachronistically'
    b= 'counterintuitive'
    c= 'misinterpretation'

    sort=[ ]
    out=''

    for letters in c:
        sort.append(letters)
    for chars in sorted(sort):
        out +=chars    
    return len(a) > len(b)

##print(evaluate())

#you can't sort strings but you can append the characters in a list ans
#sort the list then print it out or loop through it and add it to a string
# using +=

#6
'''
Write python statements corresponding to the following:
1. Assign to variable flowers a list containing the following:
    - rose
    - bougainvillea
    - marigold
    - yucca
    - day lily
    - lilly of the valley
2. Write a boolean expression that evaluates to True if string potato is in
list of flowers and evaluate the expression
3. Assign to list thorny  sublist containing the first three object in list
flowers
4. assign to list poisonous the sublist containing of just the last object
of list flowers
5. Assign to list dangerous the concantenation of lists thorny and poisonous
'''
#7
def flowers():
    kinds=['rose','bgainvillea','marigold','day lilly','lilly of the valley']

    thorny=kinds[:3]
    poisonous= kinds[-1]
    dangerous= [ ]

    for flowers in kinds:
        if flowers in thorny:
            dangerous.append(flowers)
        elif flowers in poisonous:
            dangerous.append(flowers)
        else:
            pass
    return dangerous
    
##print(flowers())
#8
'''
answers=['Y','N','Y','Y','N','Y','Y','Y','N','Y','N','Y','Y','Y']

1. assign to variable numyes to the number of occurences in y in list ansers
2. Assign to variable numno the number of occurences of N in list answers
3. Assign to variable percentYes the percentage of strings in the answers that
are 'Y'
4. sort the list answers
5. Assign to variable f the index of the first occurence of y in sorted list
answers
'''
def yesNo():
    answers=['Y','N','Y','Y','N','Y','Y','Y','N','Y','N','Y','Y','Y']

    numYes=0
    numNo= 0
    for answer in answers:
        if answer == 'Y':
             numYes += len(answer)
        else:
            numNo += len(answer)
    print('Number of answers: {}'.format(len(answers)))
    return 'Yes {}\nNo {}'.format(numYes, numNo)
            
##print(yesNo())
#9
'''
Start by assigning to variables monthsL and monthsT a list and a tuple
respectively, both containing strings 'Jan','Feb','March','May' in that
order.
Then attempt the following with both containers:
1. Insert string april between march and may
2. Append string June
3. Pop the container
4. Remove the second item in the container
5. Reverse the order of items in the containers
6. Sort the container
'''
def months():
    months_l= ['Jan','Feb','March','May']
    months_t= ('Jan','Feb','March','May') #can't manipulate tuples so turn it into
                                          # a list
    months_l[2]='april'

    new_monthst=list(months_t)
    new_monthst[2]= 'April'

    months_l.pop(2)
    new_monthst.pop(1)

    months_l.reverse()
    new_monthst.reverse()

    months_l.sort()
    new_monthst.sort()
    
    print(new_monthst)
    print(months_l)
##months()
#10
'''
Write an expression involving a three-letter string s that evaluates to a
string whose characters of s in reverse order. If s is 'top' the
expression should evaluate to pot.
'''
def reverse(string):
    method1= string[::-1]
    method2=''

    for characters in string:
        print(characters)
##        method2= characters + method2
##    return 'Theres multiple methods to reverse a string\nMethod 1: {}\nMethod 2: {}'.format(method1, method2)
##   
##print(reverse('pot'))

#11
'''
The range of a list of numbers is the largest difference between any two
numbers in a list. Write a python expression that computes the range of a list
of numbers. If the list is [3,7,-2,12] the expression should eval to 14. 
'''

def rangeList(l1):
    rangelist= max(l1)- min(l1)
    print(rangelist)
##rangeList([3,7,-2,12])
'''
s= goodbye
Evaluate the following:
1. the first character of the string s is g
2. The seventh character of the string s is g
3. the first two characters of s is g and a
4. The nest to last character os s is x
5. The middle character of s is d
6. The first and last characters of s are equal
7. The first and last strings of s match the string 'tion'
'''
#12
def goodbye():
    s= 'goodbye'

    middle=len(s)/2
    print(s[0] == 'g')
    print(s[6] == 'g')
    print(s[0] and s[1] == 'a')
    print(s[-2] == 'x')
    print(s[int(middle)] == 'd')
    print(s[0] == s[-1])
    print(s[-1] and s[-1] == 'tion')
##goodbye()
#13
'''
start by assigning to variable grades a list containing an arbitrary
sequence of grades (strings) 'A','B','C','D' AND 'F'

lst_grades= ['B','A','C','F','D','B','A','A','C','F','B','A','A','C',]

Write a ssequence of python statements that ultimately produce a list count
that the numbers of occurences if eacg grade in list grades is in alphabetical
order.

Repeat the following using a tuple of grades
tup_grades=('B','A','C','F','D','B','A','A','C','F','B','A','A','C',)
'''
#14
def countAlpha():
    lst_grades= ['B','A','C','F','D','B','A','A','C','F','B','A','A','C']
    sort_grades= sorted(lst_grades)
    A= 0
    B= 0
    C= 0
    D= 0
    F= 0
    for i in range(len(sort_grades)):
        if sort_grades[i] == 'A':
            A +=1
        elif sort_grades[i] == 'B':
            B +=1
        elif sort_grades[i] == 'C':
            C+= 1
        elif sort_grades[i] == 'D':
            D+=1
        else:
            F+=1
    count_grades=[A,B,C,D,F]
##print(countAlpha())

#15
'''

Write the relevant python expression or statement involving a list of numbers
and using list operators and methods for these specifications:

1. An expression that evaluates to the index in the middle element of lst
2. an expression that evaluates to the middle element of lst
3. An expression that sorts the list in descending order
4. An expression that removes the first number of lst lst and puts it at the end
5. 
'''
def change():
    list1=[1,2,3,4,5,6,7]

    middle= len(list1)/2
    mid_element= list1[int(middle)]
    sort_l= sorted(list1)
    sort_l.reverse()

    list1[0],list1[-1]=list1[-1], list1[0]
    print(list1)
    
##change()

'''
Takeaways: The equality operator is a powerful thing. You can assign multiple
things depending on how you use it. like lists and the studd above which is
indexing/ swapping items based on the index and equating them.
'''
#16
'''
Add one or more pairs of parenthesis to each expression so that it evaluates to
True:
a. 0==1==2
b. (2+3) == 4+(5) ==7
c. 1 < -1 == 3 > 4
'''
#17
'''
Implement a program that requests 4 numbers from the user. Your program should
compute the average of the first three numbers and compare the average to the
fourth number. If they are equal; you should PRINT equal
'''
def requests():
    try:
    
        num1= int(input('Enter a number: '))
        num2= int(input('Enter a number: '))
        num3= int(input('Enter a number: '))
        num4= int(input('Enter a number: '))

        ave= (num1+num2+num3)/3
        if num4 == ave:
            print('The average is {} and num4 is {} so expression is True'.format(round(ave,2),
            num4))
        print( 'The average is {} and num4 is {} so expression is False'.format(round(ave,2),
        num4))
    except ValueError:
        print('Error:\nCannot calculate\nYou must enter an integer')
##requests()
#18
'''
Implement a program that requests a nonempty list from the ser and PRINTS on the
screen a message giving the first and last element in the list
'''
def evalList(list1):
    return 'The first element is: {}\nThe last element is: {}'.format(list1[0],list1[-1])
##print(evalList(['fuck','this','shit']))

#19
'''
Implement a program that requests an integer n from the user and prints on the
screen the squares of all numbers from 0 up to but not including n
'''
def multiply():
    num= int(input('Enter a number: '))
    
    for i in range(num):
        print(i**2,end=' ')
##multiply()
#20
'''
Implement function reverse_string that takes an input a three letter string and
returns the string with its characters reversed.
'''
def reverse_string(string):
    if len(string) == 3:
        print(string[::-1])
    else:
        print('input was not 3 characters')
##reverse_string('fuck')
#21
'''
Implement funtion pay() that takes input 2 arguments:
    - hourly wage
    - number of hours the employee worked last week
    - your function should compute and return the employee's pay
    - Any hours worked beyond 4- is overtime and should be paid
    at 1.5 times the regular hourly wage.
'''
def pay(wage, hours):
    
    if hours > 40:
        regpay= wage* hours
        overtime= (hours-40)*wage
        weeklypay= regpay + overtime
        return weeklypay
    else:
        weeklypay= wage *hours
        return weeklypay
##print(pay(13.50,25))

#22
'''
Write a program that requests a positive four digit integer from the user
and prints its digits. You are not allowed to use the string data types
to do this task. Your program should simply read the input as integer and
processes it as an integer using standard arithemetic operations  

'''
def positive(num):
    try:
        if abs(num) >= 1000:
            print(num)
        else:
            print('Not a four digit number')
    except:
        print('You must enter an integer')
##positive('4992SRT')
#23
'''
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

'''
def password(list1):
    low= 'abcdefghijklmnopqrstuvwxyz'
    high= low.upper()
    num= [1,2,3,4,5,6,7,8,9,0]
    char= '#$@%^&*()!'

    accepted=[ ]
    
    for characters in list1:
        for letters in characters:
            if letters in low and high and num and char:
                accepted.append(characters)
    return accepted
            
##print(password(['Az09!#', 'PP','##!Po89' ]))
'''
Important takeways from this problem:
Instead of evaluating each word: evaluate each character in each word
then assess if those characters are in the condition. Using 'and'.
'''
#Section 7

'''
Write a function stats() that takes one input argument: Name of the text file
The function should print on the screen:
1. the number of lines
2. words and
3. characters in the file
your function should only open it once
'''
def stats(filename):
    infile= open(filename,'r')
    readfile= infile.readlines() #returns a list
    infile.close

    word= [ ]
    chars= [ ]
    lines= len(readfile)

    for sentences in readfile:
        cleanfile=sentences.replace('\n','')
        splitfile= cleanfile.split(' ')
        for words in splitfile:
            word.append(words)
            for letters in words:
                chars.append(letters)
    word.remove('')
    return 'Lines: {}\nWords: {}\nLetters: {}'.format(lines,len(word),len(chars))
   
##print(stats('/Users/carahvillacampa/Downloads/testing2.txt'))

'''
Write function vowel count() that takes a string as input and counts and prints
the number of occurences of vowels in the string
'''
def countVow(string):
    vowels= 'aeiou'

    vow_count= 0
    for letters in string.lower():
        if letters in vowels:
            vow_count +=1
    return 'number of vowels {}'.format(vow_count)
##print(countVow('daniel'))
'''
Write a function month that takes a number between 1 and 12 as input and returns
the three character abbreviation of the corresponding month. Do this without
an if statement, just string operations
'''

def month(num):

    months= ['January','Febuary','March','April','May','June'
             ,'July','August','September','October','November','December']
    month=[ ]
    for i in range(len(months)):
        return months[num-1]
##print(month(2))

'''
Chap 5
Write a function called geometric that takes a list of integers as input
and returns True f the integers in the list form a geometric sequence.
geo= [2,4,8,16,32]
'''


'''
Chap 5
develop a function many() that takes an input te name of a file in the current
directory and ouputs the number of words of length 1,2,3 and 4
Words of length 1: 4
'''
def many(filename):
    infile=open(filename,'r')
    read=infile.read().strip()
    infile.close

    lst_wrds= read.split()

    one=[ ]
    two=[ ]
    three=[ ]
    four=[ ]

    for words in lst_wrds:
        if len(words) == 1:
            one.append(words)
        elif len(words) == 2:
            two.append(words)
        elif len(words) ==3:
            three.append(words)
        else:
            four.append(words)
    return 'words of length \n1: {}\n2: {}\n3: {}\n4 or more: {}'.format(len(one),
    len(two),len(three),len(four))
##print(many('/Users/carahvillacampa/Downloads/testing2.txt'))
'''
Chap 5
Write a function called subset sum() that takes as input a list of positive
numbers and a positive number target.
1. your function should return True
if there are three numbers in the list that add up to target.
Eg:[5,4,10,20,15,19]
2. if not, it shuld return False
'''


'''
Chap 5
An inversion sequence is a pir of entries that are out of order.
For example, the characters F and D form an in inversion in 'ABBFHDL'
because F appears before D.
1. The number of pairs out of order is a meausre of how unsorted the
sequence is.
Inversions('abcd')= 0
Inversions('DCBA')= 4

'''


''' 
Chap 6
Implement function names() that takes no input and repeatedly ask the user to
enter the first name of a student in class. When the user enters and empty
string, the function should print for every name the number of students with
that name
'''


'''
Chap 6
Implement the function look up () that implements a phonebook lookup application
your function takes as input a dict representing a phonebook. With tuples as
keys are mapped to phone numbers as values. 
'''
phonebook={('daniel','ivan'):3125431429,('carah','villa'):6788997654,
               ('kiki','bahug ilok'):3125436789}
def lookup(dictionary):
   
    first= input('Enter first name: ')
    last= input('Enter last name: ')

    
    for keys in dictionary:
        if keys== (first.lower(), last.lower()):
            print(dictionary[keys])
##lookup(phonebook)
'''
Chap 6
Implement the function word count that takes input a string and prints the
frequency of each word in the text. Assume one with no punctuation
word appears x times
'''
def same(sentence):
    split= sentence.split()
    same=[ ]

    for i in range(len(split)):
        if split[i] == split[i-1]:
            same.append(split[i])
    return '{} appears {} times'.format(same, split.count(same[0]))

##print(same('fuck the fat fuck'))
'''
Chap 8
Implement class worker's name as a string and te hourly pay rate(as number)
1. changeRate() takes the new pay rate as input changes the worker's pay rate
the new hourly rate
2. pay() takes the number of hours worked as input 'not implemented'
'''

class WorkersPay:
    def __init__(self, name, rate):
        self.name= name
        self.rate= rate
    def changeRate(self, amount):
        self.amount= amount
        self.rate = self.amount
    def pay(self, hours):
        self.hours= hours
        hourly_pay= self.hours*self.rate
        return hourly_pay
##cara=WorkersPay('bitch',13.50)
##cara.changeRate(20)
##print(cara.pay(40))
        
'''
Chap 8
Write a container class called PriorityQueue that supports these methods:
1. insert(): tkaes a number as input and adds it to the container
2. min (): returns the smallest number in the container
3. removeMin(): removes the smallest number in the container
4. isempty(): returns True if it's empty

'''
class PriorityQueue:
    def __init__(self):
        self.list1=[ ]
    def insert(self, number):
        self.number= number
        self.list1.append(self.number)
    def min(self):
        self.min= min(self.list1)
        return self.min
    def removeMin(self):
        self.remove= self.list1.remove(self.min)
        return self.remove
    def __len__(self):
        return len(self.list1)
    def __str__(self):
        return str(self.list1)
##l1=PriorityQueue()
##l1.insert(3)
##l1.insert(5)
##l1.insert(7)
##l1.insert(8)
##print(l1.min())
##print(l1)
##print(len(l1))

'''
Chap 8
develop a class BankAccoutn that supports methods:
1. __init__(): initializes the bank account balance to the value of the
input argument of to 0 if no input argument is given
2. withdraw() takes an amount as input and withdraws it from the balance
3. deposit() takes argument as input and adds it to the balance
4. balance() return sthe balance of the account

conditions:
1. balance with a negative account can't be created
2. wthdrawal amount is greater than the balance
3. deposit amount is negative

** Modify so that a ValueError exception is thrown for any of these
violations, together with the appropriate message:
'Illegal balance','Overdraft' or 'Negative deposit'

other conditions:
1. define new exception classes:
    - NegativeBalanceError()
    - OverdraftError() and
    - DepositError()

Eg: x.deposit(-4)
will generate: deposit error: negative deposit -3
'''

class Bankaccount1:
    def __init__(self,bal= 0):
            self.bal= bal
    def withdraw(self, amount):
        self.bal -= amount
    def deposit(self,amount):
        self.bal += amount
    def balance(self):
        try:
            if self.bal >= 0:
                return self.bal
            else:
                return 'Illegal balance'
        except:
            pass
##daniel= Bankaccount1(-896)
##print(daniel.balance())


'''
Recursion
'''
def count(num):
    if num <=0:
        print('fuck')
    else:
        print(num)
        count(num-1)

def vertical(num):
    if num <10:
        print(num)
    else:
        vertical (num//10)
        print(num%10)
        
def cheers(n):
    if n <=0:
        print('Hurray!!!', end=' ')
    else:
        print('Hip', end=' ')
        cheers(n-1)
##cheers(4)
'''
Implement the container class Stat() that stores a sequence of numbers and
provides 
'''









