#Erica Filgueras CSC243: Homework 5

'''
Pseudocode:
1. open file, readlines(to return a list), close
2. separate each group in the list by commas
3. replace newline characters with an empty space
4. assign index values of the nested lists and place it in empty dictionary
5. use new dictionary for second function
6. assign variables with format strings
7. return those variables
8. place try and except blocks to check for unknown numbers
'''
def createStudentDictionary():
    'Problem 1'
    infile=open('class_roster.txt','r')
    readfile= infile.readlines()
    infile.close()
    
    dct= {}

    for names in readfile:
        cleanname= names.replace('\n','')
        splitfile= cleanname.split(',')

        firstname= splitfile[0]
        lastname=splitfile[1]
        schoolyear= splitfile[3]
        studentID= splitfile[2]
        
        dct[studentID]=(firstname,lastname,schoolyear)
    def studentsearch(dct,studentID):
        'Problem 2'
        try:
            first='Firstname: '+ '{}'.format(dct[studentID][0])
            last='Lastname: '+'{}'.format(dct[studentID][1])
            year='Year: '+'{}'.format(dct[studentID][2])
            result= first+ '\n'+ last+ '\n'+ year
            return result
        except KeyError:
            msg= 'No student with ID number: '+ studentID + '.\n'
            return msg
    print(studentsearch(dct,'16754'))
createStudentDictionary()
