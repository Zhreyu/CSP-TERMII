# Write a program in python to create a stack “student” with details of student
# name and their marks. Write Operation for Push, Pop and Traversal operation
# using menu
# Shreyas XII-B 52 (2021-2022)
student = [] # intializing stack
top = None

# creating required functions 

def isEmpty(dum):
    if dum ==[]:
        return True
    else:
        return False

def push(dum, item):
    dum.append(item)
    top = len(dum) - 1

def pop(dum):
    if isEmpty(dum):
        return 'UnderFlow!!'
    else:
        i = dum.pop()
        if len(dum)==0:
            top = None
        else:
            top = -1
    return i

def peek(dum):
    if isEmpty(dum):
        return'UnderFlow!!'
    else:
        top=len(dum)-1
        return dum[top]

def display(dum):
    if isEmpty(dum):
        print('Stack is empty!!')
    else:
        print("['NAME', 'MARKS']")
        print('------------------')
        top = len(dum)-1
        print(dum[top],'<---- TOP')
        for k in range(top-1,-1,-1):
            print(dum[k])
# menu function
def menu():
    print('--------------------------------------')
    print('MAIN MENU')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Traversal')
    print('5. Exit')
    print('---------------------------------------')

    op = int(input('ENTER CHOICE (1-5) : '))
    if op == 1:
        Name = (input('Enter Student NAME : '))
        Marks = input('Enter Student MARKS : ')
        Item = [Name,Marks]
        push(student,Item)
        print(Item,'added sucessfully!!')
        input('Press any key to continue... ')
        menu()

    elif op == 2:
        item=pop(student)
        if item == 'UnderFlow!!':
            print('UnderFlow!! Stack is Empty!')
        else:
            print(item,'is popped')
        input('Press any key to continue... ')
        menu()

    elif op == 3:
        item=peek(student)
        if item == 'UnderFlow!!':
            print('UnderFlow!! Stack is Empty!')
        else:
            print(item,'is at the top')
        input('Press any key to continue... ')
        menu()

    elif op == 4:
        display(student)
        input('Press any key to continue... ')
        menu()
    elif op ==5:
        pass
    else:
        print('NOT A VALID INPUT')
        menu()
menu()   # calling menu      
