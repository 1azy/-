

class Stack():
    def __init__(self):
        self.lists= []

    def push(self, num):
        self.lists.append(num)

    def pop(self):

        # x = self.lists[-1]
        # self.lists.remove(self.lists[-1])
        x ,self.lists = self.lists[-1],self.lists[:-1]
        return x


q = Stack()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())
