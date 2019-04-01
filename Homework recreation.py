#Homework recreation:

#Homework 1:

'''
Problem 1

Write a function that accepts 2 lists of numbers
- adds the lowest number from each list and returns the sum
'''
def lowest(l1,l2):
    min_l1= min(l1)
    min_l2= min(l2)

    sum_lowest= min_l1+min_l2
    return sum_lowest

'''
Problem 2

Write a function that accepts 2 lists of numbers, and returns the average
of the last number in each list
'''

def aveList(l1,l2):
    last_l1= l1[-1]
    last_l2=l2[-1]

    ave_lists= (last_l1+last_l2)/2
    return int(ave_lists)

'''
Write a function that accepts 2 arguments and treats them as the
non-hypoteneuse sides of a right angle triangle. (square root of the two arguments)
( 2 squared)+(3 squared)

'''
def hypo(num1,num2):
    hypoteneuse= num1**2 + num2**2
    return hypoteneuse

'''
Problem 4

Create an empty list. Then you will ask the under to enter 3 numbers
Ask for them one at a time and enter each into the list. It should return:
    - The highest number is:
    - The lowest number is:
    - The average is:
Include exceptions if the user doesn't enter just numbers on a list:
demanding them to lol.
'''
def sumList():
    l1=[ ]
    firstnum=int(input('Enter a number: '))
    secnum= int(input('Enter a number: '))
    thirdnum= int(input('Enter  a number: '))

    l1=[firstnum,secnum,thirdnum]
    maxnum= max(l1)
    minnum=min(l1)
    ave= sum(l1)/3

    return 'Highest number is: {}\nLowest number is:{}\nAverage: {}'.format(maxnum,
    minnum,int(ave))


'''
Problem 5
Write a function that accepts a list of strings and returns a single string
that is a concantenation of the entire list.
'''

def stringList(l1,string1):
    l1.append(string1)
    return l1

#Homework 2

'''
Problem 1:

Write a function called nameSearch() that accepts two arguments:
    -user's name
    -letter
the function should return the number of times the letter appears in
the name. This function should NOT be case sensitive.
'''
def nameSearch(string1, letter):
    strlower= string1.lower()
    counter= 0

    for i in range(len(strlower)):
        if strlower[i] == letter:
            counter += 1
    return counter
'''
Problem 2:

Write a function called fileStringSearch() that accepts two arguments
    - representing a file to open
    - to accept a string
What function does:
1. return true if the string is present in the file
2. return False if not.
3. The second argument must be at least 3 characters in length.
4. If not, function should return -1.
5. not be case sensitive
'''
def fileStringSearch(filename, string):
    infile= open(filename,'r')
    readfile=infile.read().lower()
    infile.close()

    list_strings= readfile.split()

    if len(string) >= 3:
        for strings in list_strings:
            if string.lower() == strings:
                return True
        return False
    else:
        return 'String is not at least 3 characters long'
        
##print(fileStringSearch('/Users/carahvillacampa/Downloads/testing2.txt','life'))

'''
Problem 3:

Write a function called problem3() that accepts 4 arguments:
    - year, month, day, 'A'/'N'
    
if 'A': The year is: XXXX. The day is: MM/DD
if 'N': The year is: XXXX. The day is: DD/MM

(Couple of colons and periods in the string. They must appear in the returned string)
'''

def problem3(year, month, day, letter):
    if letter == 'A':
        return 'The year is: {}. The day is: {}/{}'.format(year, month,day)
    if letter == 'N':
        return 'The year is: {}. The day is: {}/{}'.format(year, day, month)
##print(problem3(2019,11,9,'N'))
'''
Problem 4:

Use exam_grades.csv

Write a function that reads everything in it.
function should return the average of all the grades
'''

# What was up with this csv file wa that since it's a comma separated value:
# it's all separated by commas. So when you iterate over the number of strings in
# the file, it'll count as a string and when you change it to an int, python will
# say there's something wrong with it. The point is, you have to split the commas
# using the split (',') function.

'''
Important takeaways for this problem:
1. csv file= split the commas
2. you can directly sum a list of numbers
3. you can specify the number of decimal places
using thefunction (round, decimal places)
'''

def examGrades():
    infile= open('/Users/carahvillacampa/Downloads/exam_grades.csv','r')
    readfile= infile.read().strip()
    infile.close()

    lst_num= readfile.split(',')

    new_numlst=[ ]
    for num in lst_num:
        new_numlst.append(int(num))

    average= sum(new_numlst)/ len(new_numlst)
    return round(average,2)   
##print(examGrades())


#Homework 3
#Note: take note functions: split() and find()

'''
Problem 1:

Write a function called listofWordsinFile
It should:
1. 2 arguments (filename, letter)
2. return a list containing all of the words in the file that contain the letter
3. not case sensitive

'''

def listofWordsInFile(filename,letter):
    infile= open(filename,'r')
    readfile= infile.read().strip().lower()
    infile.close()

    lst_words=readfile.split()

    wordlst=[ ]

    for word in lst_words:
        if letter in word:
            wordlst.append(word)
    return wordlst

##print(listofWordsInFile('/Users/carahvillacampa/Downloads/testing2.txt','a'))
'''
Problem 2:
Write a function called convertCase()
It should:
1. accepts as argument (input file, output file)
2. open the file
3. read contents
4. convert upper case to lower case and vice versa
5. output the reverse to an output file
'''

#important takeaways from this stupid problem:
'''
To add things to a string: It's important to use (+=)
If  ou just use = like if I only had file= letter.lower()
it's gonna convert individual letters and just return one letter at
the end 
'''

def convertCase(In_filename, Out_filename):
    infile= open(In_filename,'r')
    readfile=infile.read()

    file=' '
    outfile= open(Out_filename,'w')
    for letter in readfile:
        if letter.isupper():
            file +=letter.lower()
        else:
            file +=letter.upper()
    return file
            
    outfile.write(readfile)
    infile.close()
    
##print(convertCase('/Users/carahvillacampa/Downloads/testing2.txt',
##            'converted.txt'))
'''
Problem 3:

Write a function called highestLowestGrades
It should:
1. read the contents thtne close the file
2. print the highest and lowest grades in the file
    -lowest: 50; highest:100
3. output with a format string
'''

def highestLowestGrades():
    infile=open('/Users/carahvillacampa/Downloads/exam_grades.csv','r')
    readfile=infile.read().strip()
    infile.close()

    splitfile=readfile.split(',')
    newlst= []

    for num in splitfile:
        newlst.append(int(num))

    high= max(newlst)
    low= min(newlst)

    return 'Highest: {}\nLowest:{}'.format(high,low)
##print(highestLowestGrades())

#Homework 4
'''
Use exam_grades.csv
It should:
1. a menu to check for highestgrade, lowestgrade and averagegrade
2. The menu is the following:
    -1: Lowest grade
    -2: highest grade
    -3: average grade
    -4: search for a grade --> "The grade {} was present"
3. write a function checkGrades()
    -reads the stuff in exam_grades.csv and stores the contents in a string
    -prints the menu above
    -Outputs results of the user's choice.
4. getChoice() that's inside checkGrades()
'''

def Checkgrades():
    infile=open('/Users/carahvillacampa/Downloads/exam_grades.csv','r')
    readfile= infile.read().strip()
    infile.close()

    lst_nums=readfile.split(',')

    new_lstnums=[]
    for num in lst_nums:
        new_lstnums.append(int(num))
    
    def getChoice():
        choice= input('Enter 1 for lowest grade: \nEnter 2 for highest grade:\nEnter 3 for the average grade:\nEnter 4 to search grade: \n')
        if choice == '1':
            lowest= min(new_lstnums)
            return lowest
        elif choice == '2':
            highest= max(new_lstnums)
            return highest
        elif choice == '3':
            average= sum(new_lstnums)/len(new_lstnums)
            return round(average,2)
        elif choice == '4':
            userin= int(input('Enter a grade to search: '))

            if userin in new_lstnums:
                return 'The grade: {} is in the list of grades'.format(userin)
            else:
                return 'The grade: {} is not in the list of grades'.format(userin)
##    print(getChoice())
##Checkgrades()
'''
Important take aways from this function:
- you can check if numbers are in a list by typing it directly.
- If you loop it through the main list of integers, it's going to generate an error
- again, split is used to separate commas that was part of the original file; so we could
work on the number strings and convert it to integer strings
'''

#Homework 5
#Hints: make use of readlines, review exception handling

'''
Instructions:
- use the class file class_roster.txt which can be found on the files
    firstitem: First name
    second: Last name
    third: ID number
    fourth: Student year
1. make a function called createStudentDictionary(): no arguments
2. function called Student search() takes two arguments: dictionary, student Id string
3. studentSearch should search the dictionary and return as format string the student
Format:
    First name: Bitch
    Last name: Armpit
    year: junior

students= createStudentDictionary --> this should represent the dictionary
studentSearch(students, 'Id number')
4. Lastly: KEY EXCEPTION ERROR: DO NOT FORGET
   should print(' no student found with Id: ')

PC:

- Read file line by line using readlines (prints out a list)
- after that, you 

'''

def createStudentDictionary():
    infile= open('/Users/carahvillacampa/Downloads/class_roster.txt','r')
    readfile=infile.readlines()
    infile.close()

    dct={}

    for names in readfile:
        cleanfile=names.replace('\n','')
        splitfile=cleanfile.split(',')

        first=splitfile[0]
        last=splitfile[1]
        ID= splitfile[2]
        year=splitfile[3]

        dct[ID]=(first, last, year)
        
    return dct
students= createStudentDictionary()

def studentSearch(dct, idnum):
    for values in dct:
        if idnum in dct:
            return 'First name: {}\nLast name: {}\nYear: {}'.format(dct[idnum][0],
                                                dct[idnum][1],dct[idnum][2])
##print(studentSearch(students,'12287'))
    
#Homework 6
'''
Create the following methods in your class Student:
1. setmethods() for: Name, percentGrade, letterGrade
2. calcLetterGrade()
3. addBonus(): percentage bonus for your letter grade

'''
class Students:
    def setName(self, name):
        self.name= name
    def setPercentGrade(self, grade):
        self.grade= grade
    def calcLetterGrade(self):
        if self.grade >= 90:
            return 'A'
        elif self.grade>= 80:
            return 'B'
        elif self.grade>= 70:
            return 'C'
        else:
            return 'D'
    def addBonus(self,percent):
        self.percent= percent
        self.grade += (self.percent/100)* self.grade
        return self.grade
    def printStudentInfo(self):
        return 'Name: {}\nPercent Grade: {}\nLetter Grade: {}'.format(self.name,
                                        self.grade,Students.calcLetterGrade(self))
##student1=Students()
##student1.setName('Ms. knees')
##student1.setPercentGrade(72)
##student1.addBonus(20)
##print(student1.printStudentInfo())

#Homework 7
'''
Create 3 classes:
    - Vehicle (parent class)Variables:mode, maxPassengers, odometer
    - Car (daughter class)= Ev: make, model, color
    - Boat (daughter class)= Ev: length, horsepower
has to output using just print:
    The mode of transport is: air
    Can carry up to: 5
    Odometer: 4500

another note: print(v1.odometer) == 2500
'''

class Vehicle:
    def __init__(self, mode, maxPassengers, odometer):
        self.mode= mode
        self.maxPassengers= maxPassengers
        self.odometer= odometer
    def odometerAdd(self, amount):
        self.odometer += amount
        return self.odometer
    def __str__(self):
        return self.mode
    def __str__(self):
        return self.maxPassenger
    def __str__(self):
        return self.odometer
    def __str__(self):
        return 'The mode of transport is: {}\nMax Passengers: {}\nOdometer:{}'.format(self.mode,
        self.maxPassengers,self.odometer)
    def __eq__(self, other):
        return (self.mode == other.mode and self.maxPassengers == other.maxPassengers
                and self.odometer== other.odometer)
class Car(Vehicle):
    def __init__(self,mode, maxPassengers,odometer,make, model,color):
        super().__init__(mode,maxPassengers,odometer)
        self.make= make
        self.model= model
        self.color= color
    def __str__(self):
        return self.make
    def __str__(self):
        return self.model
    def __str__(self):
        return self.color
    def __str__(self):
        return 'mode: {}\nMax passengers: {}\nOdometer: {}\Make: {}\nModel: {}\nColor: {}'.format(self.mode,
        self.maxPassengers,self.odometer,self.make,self.model,self.color)
    def __eq__(self,other):
        return self.make== other.make and self.model==other.model and self.color==other.color
class Boat(Vehicle):
    def __init__(self,mode,maxPassengers,odometer, length,horsepower):
         super().__init__(mode,maxPassengers,odometer)
         self.length= length
         self.horsepower= horsepower
    def __str__(self):
        return self.length
    def __str__(self):
        return self.horsepower
    def __str__(self):
        return 'mode: {}\nMax passengers: {}\nOdometer: {}\Length: {}\Horsepower: {}'.format(self.mode,
        self.maxPassengers,self.odometer,self.length,self.horsepower)
             
##v = Vehicle("air", 50, 14000)
##print("created vehicle instance")
##print("Running __str__ for vehicle")
##print(v)
##print()
##
##c1 = Car("ground", 5, 15000, "toyota", "camry", "red")
##print("created car (c1) instance")
##print("Running __str__ for car")
##print(c1)
##print()
##
##c2 = Car("ground", 7, 39000, "dodge", "caravan", "blue")
##print("created car (c2) instance")
##print("Running __str__ for car")
##print(c2)
##print()
##
##print("checking c1 == c2:")
##print(c1 == c2)
##print()
##
##print("testing odometerAdd(789)...")
##c2.odometerAdd(798)
##print(c2)
##print()
##
##b1 = Boat("water", 10, 10000, 15, 360)
##print("created boat (b1) instance")
##print("Running __str__ for boat")
##print(b1)
##print()
##
##b2 = Boat("water", 10, 10000, 15, 360)
##print("created boat (b2) instance")
##print("Running __str__ for boat")
##print(b2)
##print()
##
##print("checking if b1 == b2")
##print(b1 == b2)






