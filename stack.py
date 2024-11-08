class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack: # LIFO
    def __init__(self):
        self.top = None
        self.size = 0

    # O(n) - linear time
    def __repr__(self) -> str: # Returns a String of all values in the stack
        items = []
        current_item = self.top
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ', '.join(items)

    # O(n) - linear time
    def __contains__(self, value: any) -> bool: # Returns whether the specified value was found or not
        current_item = self.top
        while current_item is not None:
            if current_item.value == value:
                return True
            current_item = current_item.next
        return False

    # O(1) - constant time
    def __len__(self) -> int: # Returns the size of the stack
        return self.size
    
    # O(1) - constant time
    def push(self, value: any) -> None: # Adds the specified value at the top of the stack
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # O(1) - constant time
    def pop(self) -> any:  # Removes and returns the value from the top of the stack
        if self.top is None:
            raise IndexError('Stack is empty')
        else:
            pop_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return pop_value

    # O(1) - constant time
    def peek(self) -> any: # Returns the value from the top of the stack
        if self.top is None:
            raise IndexError('Stack is empty')
        else:
            return self.top.value

    # O(1) - constant time
    def is_empty(self) -> bool: # Returns whether the stack is empty or not
        return self.top is None
    
    # O(1) - constant time
    def clear(self) -> None: # Clears the stack
        self.top = None
        self.size = 0


if __name__ == '__main__':
    pass