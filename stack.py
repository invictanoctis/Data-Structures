class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # O(n) - linear time
    def __repr__(self) -> str:
        items = []
        current_item = self.top
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ', '.join(items)

    # O(n) - linear time
    def __contains__(self, value: any) -> bool:
        current_item = self.top
        while current_item is not None:
            if current_item.value == value:
                return True
            current_item = current_item.next
        return False

    # O(1) - constant time
    def __len__(self) -> int:
        return self.size
    
    # O(1) - constant time
    def push(self, value: any) -> None:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # O(1) - constant time
    def pop(self) -> any:
        if self.top is None:
            raise ValueError('Stack is empty')
        else:
            pop_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            return pop_value

    # O(1) - constant time
    def peek(self) -> any:
        if self.top is None:
            raise ValueError('Stack is empty')
        else:
            return self.top.value

    # O(1) - constant time
    def is_empty(self) -> bool:
        return self.top is None

if __name__ == '__main__':
    pass