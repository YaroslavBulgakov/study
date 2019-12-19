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
        #Голова или корень - это последний узел ну пока просто ее нет точнее начало слева
        self.head = None
        self.size=0
    #Проверим есть ли какие-то данные в определнной коробке
    def push(self,data):
        #Вот тут происходит следующие когда мы первый раз вставляем то естественно это будет голова и данные
        #Как бы хеад у нас постоянно затирается и в нем вроде бы всегда 1 элемент, но во втором значении содержиться как бы элемент который был до этого
        #ну на самом деле просто указатель на него то есть как бы пришла новая коробка и мы предудущую засунули во второе отделение, потом еще пришла и мы вторую коробку содержащую первую засунули
        #в третью
        #Поместили первый например он никуда не ссылкается Data1-->None
        #потом когда помещаем сторой self.head помещается в его свойство next
        self.head=ListNode(data,next=self.head)
        self.size+=1

    def __repr__(self):
        #Помним что во втором значении некст
        next_node=self.head
        res=''
        #Вот этот алгоритм применим для много
        while next_node:
            #Каждый раз вынимаем другой объект
            res+=str(next_node.data)+'-->'
            next_node=next_node.next
        return res

    def delete(self,value):
        this_node=self.head
        prev_node=None
        #Листаем
        while this_node:
            #Типа нашли нужный элемент
            if this_node.data==value:
                #Если предыдущая нода не пуста то нам нужно
                if prev_node is not None:
                    prev_node.next=this_node.next
                #Если же он пустой то значит это начальный
                else:
                    self.head=this_node.next
                self.size-=1
                return True
            #В конце уикла присваиваем предудущей ноде текущую а текущей следующую если не нашли
            else:
                prev_node=this_node
                this_node=this_node.next
        return False


    def contains(self,value):
        #В принипе также листаем если хотим найти что нибудь
        this_node=self.head
        #Так в принципе понятно мы листаем
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
        #Итак поместили первый элемент Data1 у него в нект поле будет Ноне
        #помещаем Data2  у него в некст уже будет объект Data1
        #помещем Data3 у него в поле некст будет обїект Data2 а у Data2-->Data1
        #Поулчается нектс-ноде идет на уменьшение т.е 4 prev--->3-->2 next а 4 это будет прев
        new=Double_Node(data,next=self.head)
        #Если элемент первый то соответсвенно предыдущего у него нет а следующий будет None
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
        prev=self.head
        st=''
        while prev:
            st+=str(prev.data)+'<--'+str(prev.next.data)+'-->'
            prev=prev.prev
        return st
    def print_list(self):
        next_node = self.head
        res = ''
        # Вот этот алгоритм применим для много
        while next_node:
            # Каждый раз вынимаем другой объект
            res += str(next_node.data) + '-->'
            next_node = next_node.next
        return res


#Нам не жуно создавать специально объекты этого класса они создаются в методе add класса LinkedList
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
mylist2.push('Double1')
mylist2.push('Double2')
mylist2.push('Double3')
mylist2.push('Double4')
print(mylist2)
print(mylist2.print_list())