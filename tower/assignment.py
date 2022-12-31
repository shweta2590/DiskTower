# A simple implementation of Priority Queue
# using Queue.


class MyInt(int):
    def __lt__(self, other):
        return self > other


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def size(self):
        return len(self.queue)

    # for checking if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    def get(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    def top(self):
        return self.queue[-1]

    # for popping an element based on Priority
    def delete(self):
        try:
            max_elem = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_elem]:
                    max_elem = i
            item = self.queue[max_elem]
            del self.queue[max_elem]
            return item
        except IndexError:
            print()
            exit()


def front_to_last(q, qsize):
    # Base condition
    if qsize <= 0:
        return

    # pop front element and push
    # this last in a queue
    q.insert(q.get())

    # Recursive call for pushing element
    front_to_last(q, qsize - 1)


# Function to push an element in the queue
# while maintaining the sorted order
def push_in_queue(q, temp, qsize):
    # Base condition
    if q.is_empty() or qsize == 0:
        q.insert(temp)
        return

    # If current element is less than
    # the element at the front
    elif temp <= q.front():

        # Call the stack with front of queue
        q.insert(temp)

        # Recursive call for inserting a front
        # element of the queue to the last
        front_to_last(q, qsize)

    else:

        # Push front element into
        # last in a queue
        q.insert(q.get())

        # Recursive call for pushing
        # element in a queue
        push_in_queue(q, temp, qsize - 1)


# Function to sort the given
# queue using recursion
def sort_queue(q):
    # Return if queue is empty
    if q.is_empty():
        return

    # Get the front element which will
    # be stored in this variable
    # throughout the recursion stack
    temp = q.get()

    # Recursive call
    sort_queue(q)

    # Push the current element into the queue
    # according to the sorting order
    push_in_queue(q, temp, q.size())


if __name__ == '__main__':
    myQueue = PriorityQueue()
    N = int(input())
    m = N
    disks = list(map(int, input().split()))
    res = []
    for i in range(len(disks)):
        myQueue.insert(MyInt(disks[i]))
        sort_queue(myQueue)
        while not myQueue.is_empty() and myQueue.top() == m:
            print(myQueue.delete(), end=" ")
            m -= 1
        print(" ")
