class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_start(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def print(self):
        if self.head is None:
            print('LL is empty')
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def insert_end(self,data):
        if self.head is None:
            self.head=None(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        

if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_start(2)
    ll.insert_start(43)
    ll.insert_start(34)
    ll.print()    