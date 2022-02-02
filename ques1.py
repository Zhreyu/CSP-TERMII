# Write a program in Python to create a stack name StackVow, which takes the
# elements as vowels and implement all oprations (Push, POP and Traversal) on
# stack StackVow 
# Shreyas XII-B 52 (2021-2022)

# answer : 

StackVow = [] # empty stack
top = None

def isEmpty(dum): # function to check if the stack is empty
    if dum ==[]:
        return True
    else:
        return False

def push(dum, item): # push function
    dum.append(item)
    top = len(dum) - 1

def pop(dum):        # pop function
    if isEmpty(dum):
        return 'UnderFlow!!'
    else:
        i = dum.pop()
        if len(dum)==0:
            top = None
        else:
            top = -1
    return i

def peek(dum):          # function to return only top element
    if isEmpty(dum):
        return'UnderFlow!!'
    else:
        top=len(dum)-1
        return dum[top]
 
def display(dum):        # function to print the whole stack 
    if isEmpty(dum):
        print('Stack is empty!!')
    else:
        top = len(dum)-1
        print(dum[top],'<---- TOP')
        for k in range(top-1,-1,-1):
            print(dum[k])

while True:
    print('--------------------------------------')
    print('STACK IMPLEMENTATION')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Traversal')
    print('5. Exit')
    print('---------------------------------------')

    op = int(input('ENTER CHOICE (1-5) : '))
    if op == 1:
        item = (input('Enter the item you want to push : '))
        if item in['a','e','i','o','u','A','E','I','O','U']: # checks if the input is a vowel 
            push(StackVow,item)
            print(item,'added sucessfully!!')
        else:
            print(f'{item} IS NOT A VOWEL')
        input('Press any key to continue... ')

    elif op == 2:
        item=pop(StackVow)
        if item == 'UnderFlow!!':
            print('UnderFlow!! Stack is Empty!')
        else:
            print(item,'is popped')
        input('Press any key to continue... ')

    elif op == 3:
        item=peek(StackVow)
        if item == 'UnderFlow!!':
            print('UnderFlow!! Stack is Empty!')
        else:
            print(item,'is at the top')
        input('Press any key to continue... ')

    elif op == 4:
        display(StackVow)
        input('Press any key to continue... ')
    elif op ==5:
        break
    else:
        print('NOT A VALID INPUT')
        


