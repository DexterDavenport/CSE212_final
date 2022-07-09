# Stacks
Stacks are a data structure that is use in python. This data staucture uses the LIFO (last in, first out) method. This is used as a way to prioritize the order in which task are complete within your program. 


* When do we use it

# I. Pringles Example
A good example of the LIFO rule would be to look at a can of Pringles. With this, the factory will load all of the chips into a cylinder can. The first chip in the can will go to the very bottom. Every following chip will be placed on top of the previous chip. With this, the first chip that the consumer can access is the last chip that was placed into the can. The last chip in is the first chip out. 

<img src="pringles.jpeg" alt="pringles" width="300" />

# II. Terms
Some of the terms that you need to understand when working with stacks are Push, Pop, Front, and Back

* Big-O
* Push - This is when you place an item into the stack
* Pop - This is when you remove an Item from the stack
* Front - Using the Pringle example, this would be the bottom of the can/ the first chips placed into the can
* Back - This refers to the side with the most recent items added to the stack

<img src="terms.jpeg" alt="terms" width= "300"/>

# III. Coding With Stacks
Working with stacks is not that difficult. In fact, there is a chance that you have already used this method before without knowing. To understand how to use stacks in python we need to lay the groundwork. 

First off, creating the stack. This can be done by typing the name you want for the stack, an equal sign, then an empty bracket.

``` python
stack = []
```

</details>

<details>
<summary>Filling the Stack While Creating It</summary>

You could also fill the stack from here like so:

``` python
stack = ['A', 'B', 'C']
```

In this example, 'A' would be the Front of the stack with 'C' as the Back.
</details>
<br />
If we were to push an item to the empty list above, we would use the 'append' operation. Append adds an item to the back of the stack. This can be done using this method.

``` python
stack = []
stack.append('A')
# If we were print stack from this point it would display "['A']"
```
If we wanted to remove an item from a stack, we would use the 'pop' operation. This will remove the most recent item added to the stack. This can be done using the following method:
``` python
stack = ['A', 'B', 'C']
stack.pop()
# If we were print stack from this point it would display "['A', 'B']"
```

<br />
<details>
<summary>Extra 'pop' Information</summary>

Note: You can also place a number inside the parenthesis to remove the item in that spot
``` python
stack = ['A', 'B', 'C']
# stack = [0, 1, 2]
stack.pop(1)
# If we were print stack from this point it would display "['A', 'C']"
```
</details>
<br />
<details>
<summary>Extra Operations To Use With Stacks:</summary>

``` python
stack = ['A', 'B', 'C']
len(stack) # This will return the number of items in the stack.

for i in stack: 
    print(i) #This will iterate through each item in the stack individually 

stack.clear() # This will remove all items from the stack
```
</details>

[Full Code Example](stacks.py)
<br />
# III Practice Code
In this example I would like you to take this code and attempt to solve it on your own before looking at the solution. 

``` python
'''
For this activity, you are going to populate this code to add the phrase 'This code 
is successful' to a stack ONE WORD AT A TIME. You will then remove that phrase ONE
WORD AT A TIME. You will start with an empty list and end with an empty list.

Hint: You could use a for loop to remove each item from the list. 
        EXP: for i in range(len(stack)):
'''

def add_remove(stack):
    print(stack)

    # Add to stack below here
    
    # Add to stack above here

    print(*stack, sep = " ") # print each item in the stack with a space between

    # Remove from stack below here
    
    # Remove from stack above here

    print(stack)
stack = []
add_remove(stack)

```


<details>
<summary>Solution</summary>

Note: This is not the only solution. You may have done this differently. As long as you followed all of the criteria, that is okay. 

In this solution you can see that I added each item to the stack one at a time using the append function. When you do not already have a list of the items (and the items being added are a small number like this), this is one of the best ways to place each item in the stack. 

When I was removing the items from the stack, you can see that I used a for loop. In this specific example I used 'for i in range(len(stack)):' This made it so that the for loop would count the number of items in the stack and run the loop that number of times. Each time it ran I removed the item at the back of the list until there were no more items left. I also added a print statement so you can see the sentence get shorter every time it runs.

``` python
'''
Creator: Dexter Davenport
CSE 212
June 30, 2022
'''
'''
For this activity, you are going to populate this code to add the phrase 'This code 
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
        print(*stack, sep = " ")

    print(stack) # confirm that the stack is empty

stack = [] # create the empty stack to pass into the function
add_remove(stack)
```
</details>




----------
Sources Used:

[CIT 212 - W03 Prepare: Reading](https://byui-cse.github.io/cse212-course/lesson03/03-prepare.html#1.4)

[Pringles](https://p.turbosquid.com/ts-thumb/Zk/I5lyY1/ix/open_pringles_original_potato_chips_small_can_360/jpg/1633470052/600x600/turn_fit_q87/725646f9af3dac2f58fefe82ce81331341809af1/open_pringles_original_potato_chips_small_can_360-1.jpg)

[Stacks Image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/2000px-Data_stack.svg.png)