class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key==data:
            print(f'{data} is found')
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f'{data} is not present ')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f'{data} is not present')
    
if __name__ == '__main__':
    root=BST(None)
    list1=[10,5,15,20,12,5,17,4,7,8]
    for num in list1:
        root.insert(num)
    root.search(7)
    root.search(50)
        