# Write a python program to create stack Sport_Stack to store age of sportsman
# using stack implementation as list. Write Operation for Push, Pop and Traversal
# operation using menu

# answer :
Sport_Stack = []
top = None

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
    print('Sportsman Age')
    print('---------------')
    if isEmpty(dum):
        print('Stack is empty!!')
    else:
        top = len(dum)-1
        print(dum[top],'<---- TOP')
        for k in range(top-1,-1,-1):
            print(dum[k])

def menu():
    print('--------------------------------------')
    print('-----MENU----')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Traversal')
    print('5. Exit')
    print('---------------------------------------')

    op = int(input('ENTER CHOICE (1-5) : '))
    if op == 1:
        item = (input('Enter the Age of Sportsman : '))
        push(Sport_Stack,item)
        print(item,'added sucessfully!!')
        input('Press any key to continue... ')
        menu()

    elif op == 2:
        item=pop(Sport_Stack)
        if item == 'UnderFlow!!':
            print('UnderFlow!! Stack is Empty!')
            menu()
        else:
            print(item,'is popped')
        input('Press any key to continue... ')
        menu()

    elif op == 3:
        item=peek(Sport_Stack)
        if item == 'UnderFlow!!':
            print('UnderFlow!! Stack is Empty!')
            menu()
        else:
            print(item,'is at the top')
        input('Press any key to continue... ')
        menu()

    elif op == 4:
        display(Sport_Stack)
        input('Press any key to continue... ')
        menu()
    elif op ==5:
        pass   
    else:
        print('NOT A VALID INPUT')
        menu()
menu()