class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    # O(n) - linear time
    def __repr__(self) -> str:
        if self.head is None:
            return '[]'
        else:
            last = self.head
            return_string = f'[{last.value}'
            while last.next:
                last = last.next
                return_string += f', {last.value}'
            return_string += ']'
            return return_string

    # O(n) - linear time
    def __contains__(self, value: any) -> bool:
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False   

    # O(1) - constant time
    def __len__(self) -> int:
        return self.size

    # O(1) - constant time
    def append(self, value: any) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node
        self.size += 1

    # O(1) - constant time
    def prepend(self, value: any) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node
        self.size += 1

    # O(n) - linear time
    def insert(self, value: any, index: int) -> None:
        if index == 0:
            self.prepend(value)
        elif index >= self.size:
            self.append(value)
        else:
            if self.head is None:
                raise ValueError('Index out of bounds')
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError('Index out of bounds')
                    last = last.next
                
                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                self.size += 1

    # O(n) - linear time
    def delete(self, value: any) -> None:
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
                if self.head:
                    self.head.previous = None
                else:
                    self.tail = None
                self.size -= 1
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next == self.tail:
                            self.tail = last
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        self.size -= 1
                        break
                    last = last.next
                else:
                    raise ValueError('Value is not in List')
        else:
            raise ValueError('List is empty')

    # O(n) - linear time
    def pop(self, index: int) -> any:
        if self.head is None:
            raise ValueError('List is empty')
        elif index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
            self.size -= 1
            return value
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError('Index out of bounds')
                last = last.next
            if last.next is None:
                raise ValueError('Index out of bounds')
            value = last.next.value
            if last.next.next is not None:
                last.next.next.previous = last
            last.next = last.next.next
            if last.next is None:
                self.tail = last
            self.size -= 1
            return value

    # O(n) - linear time
    def get(self, index: int) -> any:
        if self.head is None:
            raise ValueError('Index out of bounds')
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError('Index out of bounds')
                last = last.next
            return last.value

if __name__ == '__main__':
    pass