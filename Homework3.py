#Erica Filgueras CSC 243

#Pseudocode for Problem 1:
'''
1. open file and read file as big string split big string to a list of strings
2. convert list of strings to lowercase
3. Create a variable1 then store second argument to that variable
to use for the loop
4. Create a variable2 for an empty list to store list of words
5. specify that variable2 also has to be lowercase
6. Use for loop with variable one then use conditional to examine if second
argument is in first
7. add the word to the empty list
'''
def listofWordsinfile(Filename, letter):
    'Problem 1'
    Infile= open(Filename,'r')
    Infile_read= Infile.read()
    Infile.close()

    lowerfile=Infile_read.lower()
    splitfile=lowerfile.split()

    keyletter=letter.lower()

    keylist=[]

    for word in splitfile:
        if keyletter in word:
            keylist.append(word)
    print(keylist)

   
listofWordsinfile('/Users/carahvillacampa/Downloads/testing2.txt','R')

#Pseudocode for Problem2:
'''
1. open file, read the contents where it should convert all lower to upper
and vice versa
2. evaluate each character in word
3. Find any upper/lower case characters and convert it to the opposite
4. Assign to a variable
5. open an output file and write it there
'''

def convertCase(infilename,outfilename):
    'Problem 2'
    
    infile=open('infilename','r')
    readfile=infile.read()
    infile.close()

    splitfile=readfile.split()
    invertcase=' '
   

    outfile=open('outfilename','w')
    
    for word in splitfile:
        for letter in word:
            if letter.islower():
                invertcase +=str(letter.upper())
            else:
                invertcase +=str(letter.lower())
               
    outfile.write(invertcase)
    outfile.close()
                    
convertCase()


#Pseudocode for Problem 3
'''
1. open file, read then close
2. Use eval function for it to be read as an expression
3. use max and min function and assign it to variables

'''

def highestLowestgrades():
    'Problem 3'
    exam=open('/Users/carahvillacampa/Downloads/exam_grades.csv','r')
    examread= exam.read()
    exam.close()

    evalexam= eval(examread)

    maxexam=max(evalexam)
    print('The highest grade is: '+'{}'.format(maxexam))
    minexam=min(evalexam)
    print('The lowest grade is: '+ '{}'.format(minexam))

highestLowestgrades()
