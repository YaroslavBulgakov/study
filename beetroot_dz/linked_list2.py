class Stack():
    def __init__(self):
        self.list=[]
    def push(self,data):
        self.list.append(data)
    def pop(self):
        return self.list.pop()
    def get(self):
        return self.list

mystack=Stack()
mystack.push('Data1')
mystack.push('Data2')
print(mystack.pop())
print(mystack.get())

class ListNode:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size=0
    def push(self,data):
        self.head=ListNode(data,next=self.head)
        self.size+=1

    def __repr__(self):
        next_node=self.head
        res=''
        while next_node:
            res+=str(next_node.data)+'-->'
            next_node=next_node.next
        return res

    def delete(self,value):
        this_node=self.head
        prev_node=None
        while this_node:
            if this_node.data==value:
                if prev_node is not None:
                    prev_node.next=this_node.next
                else:
                    self.head=this_node.next
                self.size-=1
                return True
            else:
                prev_node=this_node
                this_node=this_node.next
        return False


    def contains(self,value):
        this_node=self.head
        while this_node:
            if this_node.data==value:
                return True
            this_node=this_node.next
        return False


class Double_Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new=Double_Node(data,next=self.head)
        '''
        if self.head is None:
            new.prev=None
        if self.head:
            self.head.prev=new
        self.head=new
        '''
        if self.head:
            self.head.prev = new
        self.head = new
    def __repr__(self):
        this_node=self.head
        st=''
        while this_node:
            if this_node.prev and this_node.next:
                st+='<--'+str(this_node.data)+'-->'
            elif this_node.next:
                st+=str(this_node.data)+'-->'
            elif this_node.prev:
                st += '<--' + str(this_node.data)
            else:
                st+=str(this_node.data)
            this_node=this_node.next

        return st

    def delete(self,value):
        this_node=self.head
        next_node=None
        prev_node=None
        while this_node:
            if this_node.data==value:
                if this_node.prev:
                    this_node.prev.next=this_node.next
                if this_node.next:
                    this_node.next.prev=this_node.prev
                return True
            this_node=this_node.next
        return False
    def contains(self,value):
        this_node=self.head
        while this_node:
            if this_node.data==value:
                return True
            this_node=this_node.next
        return False
    def print_one_linked_list(self):
        next_node = self.head
        res = ''

        while next_node:

            res += str(next_node.data) + '-->'
            next_node = next_node.next
        return res


print('------------Linked list--------------')
mylist=LinkedList()
mylist.push('Data1')
mylist.push('Data2')
mylist.push('Data3')
mylist.push('Data4')
print(mylist)
print(mylist.contains('Data1'))
print(mylist.contains('Data5'))
mylist.delete('Data2')
print(mylist)

print('---------Double Linked List----------')
mylist2=DoubleLinkedList()
for i in range(1,8):
    mylist2.push('Double{0}'.format(i))
print(mylist2)

print('List contains Double3? ',mylist2.contains('Double3'))
print('List contains Test? ',mylist2.contains('Test'))
#print(mylist2.print_list())
print('Delete Double3',mylist2.delete('Double3'))
print(mylist2)
print('Delete Double1',mylist2.delete('Double1'))
print(mylist2)