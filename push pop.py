class Stack:
    def __init__(self):
        # Initialize an empty list to use as the stack
        self.stack = []

    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        # Remove and return the top item from the stack if it's not empty
        if not self.is_empty():
            item = self.stack.pop()
            print(f"{item} popped from stack")
            return item
        else:
            print("Stack is empty")

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def display(self):
        # Display the current items in the stack
        print("Stack:", self.stack)

def menu():
    # Create an instance of the Stack class
    stack = Stack()
    while True:
        # Display the menu options
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Display Stack")
        print("4. Exit")
        
        # Get the user's choice
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Push an item onto the stack
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == 2:
            # Pop an item from the stack
            stack.pop()
        elif choice == 3:
            # Display the current stack
            stack.display()
        elif choice == 4:
            # Exit the program
            print("Exiting...")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run the menu function if this script is executed
    menu()
