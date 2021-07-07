import time  
def mydecorator(f):
    def log_f_as_called():
        start = time.time()
        print(f'{f.__name__} starting time {start}')
        f()
        end = time.time()
        print(f'{f.__name__} ending time {end}')
        print(f'It took {end-start} to finish')
    return log_f_as_called
@mydecorator
def printista():
  print('A qutation')

printista()


class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None

    def __iter__(self):
        def values_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return values_generator()

    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))

    def insert(self, value):
        self.head = Node(value, self.head)

linked = LinkedList()
linked.insert(1)
linked.insert(2)
linked.insert(3)
linked.insert(4)


linked2 = LinkedList()
linked2.insert(1)
linked2.insert(2)
linked2.insert(3)
linked2.insert(4)

for val in linked :
  print(val)


if linked == linked2 :
  print('linked is equal to linked2')