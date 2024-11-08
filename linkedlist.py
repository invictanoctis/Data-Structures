class Node:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    # O(n) - linear time
    def __repr__(self) -> str:
        items = []
        last = self.head
        while last is not None:
            items.append(str(last.value))
            last = last.next
        return f"[{', '.join(items)}]"

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

    # O(n) - linear time
    def append(self, value: any) -> None:
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
    def prepend(self, value: any) -> None:
        first_node = Node(value)
        self.size += 1
        first_node.next = self.head
        self.head = first_node

    # O(n) - linear time
    def insert(self, value: any, index: int) -> None:
        if index == 0:
            self.prepend(value)
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
                self.size += 1
                new_node.next = last.next
                last.next = new_node

    # O(n) - linear time
    def delete(self, value: any) -> None:
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
            raise ValueError('List is empty')

    # O(n) - linear time
    def pop(self, index: int) -> any:
        if self.head is None:
            raise ValueError('List is empty')
        if index == 0:
            value = self.head.value
            self.head = self.head.next
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
            last.next = last.next.next
            self.size -= 1
            return value

    # O(n) - linear time
    def get(self, index: int) -> any:
        if self.head is None:
            raise ValueError('Index out of bounds')
        last = self.head
        for i in range(index):
            if last.next is None:
                raise ValueError('Index out of bounds')
            last = last.next
        return last.value

if __name__ == '__main__':
    pass