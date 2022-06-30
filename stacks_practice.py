'''
Creator: Dexter Davenport
CSE 212
June 30, 2022
'''
'''
For this activity, you are goin to populate this code to add the phrase 'This code 
is successful' to a stack ONE WORD AT A TIME. You will then remove that phrase ONE
WORD AT A TIME. You will start with an empty list and end with an empty list. 

Hint: You could use a for loop to remove each item from the list. 
        EXP: for i in range(len(stack)):
'''

def add_remove(stack):
    print(stack) # confirm that the stack is empty

    stack.append('This')
    stack.append('code')
    stack.append('is')
    stack.append('successful')

    print(*stack, sep = " ") # print each item in the stack with a space between

    for i in range(len(stack)): # 'for i in stack:' does not work, you must use a range if using a for loop in this example
        stack.pop()

    print(stack) # confirm that the stack is empty

stack = [] # create the empty stack to pass into the function
add_remove(stack)