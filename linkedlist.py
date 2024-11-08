class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    # O(n) - linear time
    def __repr__(self) -> str: # Returns a String of all values in the list
        items = []
        current_item = self.head
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ', '.join(items)

    # O(n) - linear time
    def __contains__(self, value: any) -> bool: # Returns whether the specified value was found or not
        current_item = self.head
        while current_item is not None:
            if current_item.value == value:
                return True
            current_item = current_item.next
        return False

    # O(1) - constant time
    def __len__(self) -> int: # Returns the size of the list
        return self.size

    # O(n) - linear time
    def append(self, value: any) -> None: # Adds the specified value at the end of the list
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    # O(1) - constant time
    def prepend(self, value: any) -> None: # Adds the specified value at the beginning of the list
        first_node = Node(value)
        self.size += 1
        first_node.next = self.head
        self.head = first_node

    # O(n) - linear time
    def insert(self, value: any, index: int) -> None: # Inserts the specified value at the specified index
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise IndexError('Index out of bounds')
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise IndexError('Index out of bounds')
                    last = last.next
                new_node = Node(value)
                self.size += 1
                new_node.next = last.next
                last.next = new_node

    # O(n) - linear time
    def delete(self, value: any) -> None: # Removes the specified value
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
                self.size -= 1
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        self.size -= 1
                        break
                    last = last.next
                else:
                    raise ValueError('Value is not in List')
        else:
            raise IndexError('List is empty')

    # O(n) - linear time
    def pop(self, index: int) -> any: # Removes and returns the value at the specified index
        if self.head is None:
            raise IndexError('List is empty')
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise IndexError('Index out of bounds')
                last = last.next
            if last.next is None:
                raise IndexError('Index out of bounds')
            value = last.next.value
            last.next = last.next.next
            self.size -= 1
            return value

    # O(n) - linear time
    def get(self, index: int) -> any: # Returns the value at the specified index
        if self.head is None:
            raise IndexError('Index out of bounds')
        last = self.head
        for i in range(index):
            if last.next is None:
                raise IndexError('Index out of bounds')
            last = last.next
        return last.value
    
    # O(n) - linear time
    def index(self, value: any) -> int: # Returns the first index of the specified value
        last = self.head
        index = 0
        while last is not None:
            if last.value == value:
                return index
            last = last.next
            index += 1
        raise ValueError('Value is not in list')
    
    # O(1) - constant time
    def is_empty(self) -> bool: # Returns whether the list is empty or not
        return self.head is None

    # O(1) - constant time
    def clear(self) -> None: # Clears the list
        self.head = None
        self.size = 0


if __name__ == '__main__':
    pass