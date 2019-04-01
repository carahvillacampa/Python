#Erica Filgueras: CSC 243 Homework 4


'''
Pseudocode for getfilestring()
1. Open the file, read and close the file
2. split the big string that reads the file
3. iterate through the list of strings and convert to a list of integers
4. use this as reference for getChoice() function

Pseudocode for getChoice()
1. Write a menu for options then askfor userinput
2. Write values of the options using the list of integers in getfilestring()
3. if the user enters an empty string, it's going to ask user to try again
4. if the user enters the options on the menu, it should print out the value of
of one of the options

To do this:
1. Write all true statements to a while loop
2. While loop should contain menu and user input as well as min,max and average
values generated using getChoice. This is based on a true/false statment using
a variable.
3. this loop also evaluates the values entered from the input
4. if user enetered numbers from the menu, it should print out those values
5. to break the while loop, another while loop should be created that contains
booleans
6. these booleans should evaluate user input. If empty, it should reiterate the
first while loop
7. If a value is entered from the menu, it should print out statement and not
iterate through the whole thing again

'''

def Check_grades():
    
    def getfilestring():
        'Opens file and converts big string to list of integers'
        openfile= open('exam_grades.csv','r')
        readfile= openfile.read()
        openfile.close()
        splitfile=readfile.split(',')

        intnumlst=[ ]

        for number in splitfile:
            intnumlst.append(int(number))

        def getChoice():
            'Ask for user input and evaluates it'
            statement = True
            while statement:

                menu='What would you like to search for?'+ '\n' +'Press 1 for lowest grade'+ '\n'+ 'Press 2 for the highest grade'+ '\n'+ 'Press 3 for the average'+'\n'+'Press 4 to check your grade'
                print(menu)

                userinput= input('Enter a choice: ')
                
                minlist= min(intnumlst)
                maxlist= max(intnumlst)
                avelist=sum(intnumlst)/len(intnumlst)
                roundave= round(avelist,1) #rounds average to one decimal place
           
                if userinput == '1':
                    print('The lowest grade is'+ ' '+'{}'.format(minlist))
                elif userinput == '2':
                    print('The highest grade is'+ ' '+'{}'.format(maxlist))
                elif userinput == '3':
                    print('The average grade is'+' '+'{}'.format(roundave))
                elif userinput == '4':
                    searchgrade= int(input('Enter grade to be searched: '))
                    if abs(searchgrade) in intnumlst:
                        print('The grade'+' '+'{}'.format(searchgrade)+' '+'is present')
                    else:
                        print('The grade'+' '+'{}'.format(searchgrade)+' '+'is NOT present')

                while True:
                    if userinput == ' ':
                        print('no choice was entered. Try again')
                        statement= True
                        break
                    else:
                        userinput== 'not empty'
                        statement= False
                        break
                    
        getChoice()
        
    getfilestring()

Check_grades()

