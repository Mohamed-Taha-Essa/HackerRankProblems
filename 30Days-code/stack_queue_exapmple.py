
'''
FIFO (First-In-First-Out) data structure.
'''
x =False
y =True
if x:
    from queue import Queue

    # Creating a queue
    my_queue = Queue()

    # Enqueue elements
    my_queue.put(1)
    my_queue.put(2)
    my_queue.put(3)

    # Dequeue elements
    first_item = my_queue.get()
    second_item = my_queue.get()

    print("Dequeued items:", first_item, second_item)

'''
las in first out (LIFO)
'''
if x:
    # Creating an empty stack
    my_stack = []

    # Pushing elements onto the stack
    my_stack.append(1)
    my_stack.append(2)
    my_stack.append(3)

    # Popping elements from the stack
    pop_item = my_stack.pop()
    print("Popped item:", pop_item)

    # Checking the current state of the stack
    print("Current stack:", my_stack)


'''
Alternatively, you can use the collections.deque class to implement a stack efficiently.
 The deque class provides fast O(1) appends and pops from both ends.
 
 '''
if y:
    from collections import deque

    # Creating an empty stack using deque
    my_stack = deque()

    # Pushing elements onto the stack
    my_stack.append(1)
    my_stack.append(2)
    my_stack.append(3)

    # Popping elements from the stack
    pop_item = my_stack.pop()
    print("Popped item:", pop_item)

    # Checking the current state of the stack
    print("Current stack:", my_stack)






