class Node:
    def __init__(self, val=None):
        '''
        Initialize the node
        '''

        self.left = None
        self.right = None
        self.val = val



    # Finish this function
    def insert(self, val):
        '''
        This function will allow you to insert your data into the
        tree. 
        '''

        # Check if self.val is empty, if so make it equal to the value you passed in
        if not self.val:
            self.val = val
            return
        # Check if self.val is equal to the value you passed in, if so return
        if self.val == val:
            return
        # Check to see if the number is less than the current value
        if val < self.val:
            if self.left:
                # If it is less it will call the function again recursively
                self.left.insert(val)
                return
            self.left = Node(val)
            return
        if self.right:
            # If it is greater it will call the function again recursively
            self.right.insert(val)
            return
        self.right = Node(val)

        if self.right:
            # If it is greater it will call the function again recursively
            self.right.insert(val)
            return
        self.right = Node(val)


    # Finish this function
    def in_list(self, val):
        '''
        This function will look through the whole list to see if the 
        val is in the tree. 
        '''

        # Add your code Below



        # Add your code Above


    # Finish this function
    def ordered(self, vals):
        '''
        This function will check whole left side of the tree then the 
        right side of the tree while adding each leaf to the empty list
        (vals). Checking in this order will make the list order itself 
        from smallest to biggest.
        '''

        # Add your code Below



        # Add your code Above

        

def main():
    # Create a list or random numbers
    nums = [20, 1, 19, 2, 18, 3, 17, 4, 16, 5]
    bst = Node()

    # Run the insert statement for each number in the nums list
    for num in nums:
        bst.insert(num)
    print("Unordered List: ")
    print(nums)
    print("Ordered List: ")
    print(bst.ordered([]))
    print()

    for i in range(1,10):
        print(f"Is {i} in the tree: ")
        # Check if each number in the range is or is not in the tree
        print(bst.in_list(i))

main()



'''
Unordered List: 
[20, 1, 19, 2, 18, 3, 17, 4, 16, 5]
Ordered List: 
[1, 2, 3, 4, 5, 16, 17, 18, 19, 20]

Is 1 in the tree: 
True
Is 2 in the tree: 
True
Is 3 in the tree: 
True
Is 4 in the tree: 
True
Is 5 in the tree: 
True
Is 6 in the tree: 
False
Is 7 in the tree: 
False
Is 8 in the tree: 
False
Is 9 in the tree: 
False
'''
