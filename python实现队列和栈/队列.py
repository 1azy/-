

class Queue():
    def __init__(self):
        self.lists= []

    def enqueue(self, num):
        self.lists.append(num)

    def dequeue(self):

        # x = self.lists[0]
        # self.lists.remove(self.lists[0])
        x ,self.lists = self.lists[0],self.lists[1:]
        return x


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
