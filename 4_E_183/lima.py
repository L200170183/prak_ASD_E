class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
        return self.head
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
llist = LinkedList() 
llist.pushAw(21)
llist.pushAw(22)
llist.pushAw(12)
llist.pushAw(14)
llist.pushAw(2)
llist.pushAw(19)

print(llist.search(21))
print(llist.search(29))
