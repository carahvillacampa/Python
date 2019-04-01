#Erica Filgueras: Week 2 CSC 243 Homework

def nameSearch(user,letter):
    'Problem 1'
    #arguments have to be strings
    
    u=user.lower()
    l=letter.lower()
    if l in u:
        print(u.count(l))

def filereading(filename,string):
    'Problem 2'
    #filename= relative or abs filepath (macOS)

    file1=open(filename,'r')
    readfile= file1.read()
    file1.close()
    content=readfile.split()
    for words in content:
        lowcontent= words.lower()

    string=input('Enter a word: ')
    string=string.lower()
    
    if string in content and len(string) >= 3:
        print('True')
    elif len(string) < 3:
        return -1 
    else:
        print('False')


def problem3(year, month, day, timezone):
    'Problem 3'
    # Month and timezone have to be strings

    timeformat=year, month, day
    if timezone == 'A':
        print('The day is:'+ ' '+'{}/{}'.format(month,day))
        print('The year is:'+'{}'.format(year))
    elif timezone =='N':
        print('The day is:'+ ' '+'{}/{}'.format(day,month))
        print('The year is:'+' '+'{}'.format(year))


def getAve():
    'Problem 4'

    file2= open('exam_grades.csv','r') #absolute/relative file path
    readfile2= file2.read()
    file2.close()

    splitfile=eval(readfile2)
    
    Ave= sum(splitfile)/ len(splitfile)
    print(Ave)
    
    
getAve()

#another solution:

def getAve1():

    file= open('exam_grades.csv','r')
    readfile= file.read()
    splitfile= readfile.split()
    file.close()

    for x in splitfile:
        num= eval(x)
        
    Ave=sum(num)/len(num)
    print(Ave)

getAve1()



