class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    # O(n) - linear time
    def __repr__(self) -> str: # Returns a String of all values in the queue
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ', '.join(items)

    # O(n) - linear time
    def __contains__(self, value: any) -> bool: # Returns whether the specified value was found or not
        current_item = self.front
        while current_item is not None:
            if current_item.value == value:
                return True
            current_item = current_item.next
        return False

    # O(1) - constant time
    def __len__(self) -> int: # Returns the size of the queue
        return self.size

    # O(1) - constant time
    def enqueue(self, value: any) -> None: # Adds the specified value to the rear of the queue
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    # O(1) - constant time
    def dequeue(self) -> any: # Removes and returns the value from the front of the queue
        if self.front is None:
            raise IndexError('Queue is empty')
        dequeue_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeue_value

    # O(1) - constant time
    def peek(self) -> any: # Returns the value from the front of the queue
        if self.front is None:
            raise IndexError('Queue is empty')
        return self.front.value

    # O(1) - constant time
    def is_empty(self) -> bool: # Returns whether the queue is empty or not
        return self.front is None

    # O(1) - constant time
    def clear(self) -> None: # Clears the queue
        self.front = None
        self.rear = None
        self.size = 0


if __name__ == '__main__':
    pass # type: ignore