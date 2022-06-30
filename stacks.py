# print statements to show each change

stack = ['This', 'is', 'a', 'this', 'of'] #start off with a populated stack

print(stack)

stack.append('words') # add 'words' to the back of the stack

print(stack)

for i in stack: # iterate through and print each item in the stack
    print(i)

stack.pop() # Remove the item at the back of the stack

print(stack)

stack.clear() # Remove all items from the stack

print(stack)

