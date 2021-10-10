class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node
    def prints(self):
        if self.head is None:
            print("empty list")
            return
        itr =self.head
        lists = ""
        while itr:
            lists=str(itr.data)+"-->"
            itr = itr.next
            print(lists, end='')
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        print(count)
        return count
    def remove(self,index):
        if index<0 or index>self.get_length():
            print("inavlid")
        if index==0:
            self.head=self.head.next
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    def insert_at(self,index ,data):
        if index<0 or index>self.get_length():
            print("inavlid")
        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1
if  __name__ == "__main__":
    l=linkedlist()
    l.insert_at_end(34)
    l.insert_at_end(67)
    l.insert_at_end(78)
    l.insert_at_end(89)
    l.insert_at(2,56)
    l.prints()






