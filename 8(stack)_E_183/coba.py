class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self, data):
        return self.items.append(data)
        



##myS = Stack()
##myS.push(12)
##myS.push(11)
##myS.push(324)
##myS.push(4)
##myS.push(13)
##print(myS.items)
##myS.pop()
##print(myS.peek())
