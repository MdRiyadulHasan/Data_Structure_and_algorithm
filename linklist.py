class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #insert after last node
    def insert_at_end(self,new_data):
        new_node=Node(new_data)
        # if head is none
        if self.head is None:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next:
                last_node= last_node.next
            last_node.next=new_node
    #insert at beginning
    def insert_at_beginning(self,new_data):
        new_node =Node(new_data)
        new_node.next=self.head
        self.head=new_node
    #insert_after_certain_data
    def insert_after_certain_data(self,certain_data,new_data):
        new_node=Node(new_data)
        temp_node=self.head
        while temp_node:
            if temp_node.data==certain_data:
                break
            temp_node=temp_node.next
        new_node.next=temp_node.next
        temp_node.next=new_node
    #insert_after_certain_position
    def insert_certain_position(self,pos, new_data):
        new_node=Node(new_data)
        temp_node = self.head
        for i in range(pos-1):
            temp_node=temp_node.next
        new_node.next=temp_node.next
        temp_node.next=new_node
    # delete first_node
    def delete_beginning(self):
        temp_node=self.head
        self.head=temp_node.next
        temp_node.next=None
    #delete end node
    def delete_last_node(self):
        previous_node=self.head
        temp_node=self.head.next
        if self.head is None:
            return
        else:
            while temp_node.next:
                temp_node=temp_node.next
                previous_node=previous_node.next
            previous_node.next=None
    #deletion  certain data
    def delete_certain_data(self,certain_data):
        temp_node=self.head.next
        previous_node=self.head
        while temp_node:
            if temp_node.data==certain_data:
                break
            temp_node=temp_node.next
            previous_node=previous_node.next
        previous_node.next=temp_node.next
        temp_node.next=None
    #delete after certain position 
    def delete_certain_position(self,pos):
        temp_node=self.head.next
        previous_node=self.head
        for i in range(pos-1):
            temp_node=temp_node.next
            previous_node=previous_node.next
        previous_node.next=temp_node.next
        temp_node.next=None
    # link list traversing
    def print_LinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node=current_node.next
if __name__ == '__main__':
    link_list = LinkedList()
    link_list.insert_at_end(10)
    link_list.insert_at_end(20)
    link_list.insert_at_end(30)
    link_list.insert_at_beginning(35)
    link_list.insert_at_beginning(25)
    link_list.insert_after_certain_data(20,120)
    link_list.insert_certain_position(2,105)
    link_list.print_LinkedList()
    print('\n')
    link_list.delete_beginning()
    link_list.delete_certain_position(4)
    link_list.delete_certain_data(20)
    link_list.print_LinkedList()
    
       