class Node:
    def __init__(self, val=None):
        '''
        Initialize the node
        '''

        self.left = None
        self.right = None
        self.val = val
        
    def insert(self, val):
        '''
        This function will allow you to insert your data into the
        tree. 
        '''

        # Check if self.val is empty, if so make it equal to the value you passed in
        if not self.val:
            self.val = val
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

    def in_list(self, val):
        '''
        This function will look through the whole list to see if the 
        val is in the tree. 
        '''

        # Check to see if the current value is equal the the value you are looking for
        if val == self.val:
            return True
        # Check if the value is less than the one you are looking for 
        if val < self.val:
            # If you have reached the end of the tree and have not found the value, return False
            if self.left == None:
                return False
            # If you have not found the end or the value, call the funtion again
            return self.left.in_list(val)
        # If you have reached the end of the tree and have not found the value, return False
        if self.right == None:
            return False
        # If you have not found the end or the value, call the funtion again
        return self.right.in_list(val)

    def ordered(self, vals):
        '''
        This function will check whole left side of the tree then the 
        right side of the tree. Checking in this order will make the 
        list order itself from smallest to biggest.
        '''

        # If you have not reached the end of the tree, call the function again
        if self.left is not None:
            self.left.ordered(vals)
        # If value is not none add it to the list of values
        if self.val is not None:
            vals.append(self.val)
        # If you have not reached the end of the tree, call the function again
        if self.right is not None:
            self.right.ordered(vals)
        return vals

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
