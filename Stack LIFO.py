class Stack:
    def __init__(self):
        self.stack = []

    # Push operation to add an element to the stack
    def push(self, element):
        self.stack.append(element)
        print(f"Pushed {element} to stack")

    # Pop operation to remove and return the top element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        else:
            popped_element = self.stack.pop()
            print(f"Popped {popped_element} from stack")
            return popped_element

    # Peek operation to return the top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            top_element = self.stack[-1]
            print(f"Top of the stack element is: {top_element}")
            return top_element

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return the size of the stack
    def size(self):
        size = len(self.stack)
        print(f"Current size of stack: {size}")
        return size

    # Display the current stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Current stack:", self.stack)


# Main block to interact with the stack
if __name__ == "__main__":
    stack = Stack()  # Create an instance of the Stack class

    # Take user input for pushing elements onto the stack
    n = int(input("How many elements do you want to push onto the stack: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        stack.push(element)

    # Display the stack after all pushes
    stack.display()

    # Peek the top element
    stack.peek()

    # Perform pop operations and display the stack after each pop
    stack.pop()
    stack.display()

    # Get the current size of the stack
    stack.size()

    # Check if the stack is empty
    print("Is stack empty?", stack.is_empty())

    # Perform additional pop operations to empty the stack
    stack.pop()
    stack.pop()

    # Final check for empty stack
    print("Is stack empty?", stack.is_empty())

    # Display final state of the stack
    stack.display()
