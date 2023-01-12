import node
class LinkedList:
 
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.size = 0 
    
    def __repr__(self) -> str:
         return f"(LinkedList: (Head:{self.Head}, Tail: {self.Tail}, Size: {self.size})"

    
    def append(self, data):
        nd = node.Node(data)
        if (self.Head == None):
            self.Head=self.Tail = nd
            self.size +=1

        else:
            self.Tail.Next = nd
            nd.Prev = self.Tail
            self.Tail = nd
            self.size +=1

    def insertByPos(self, pos, data):
        nd = node.Node(data)
        if(self.Head == None):
             self.Head=self.Tail = nd
             self.size +=1
        else:
            if(pos ==0):
                nd.Next = self.Head
                self.Head.Prev = nd
                self.Head = nd
                self.size +=1

            else:
                i= 0
                ptr = self.Head
                while(i< pos-1 and ptr.Next !=None):
                    ptr = ptr.Next
                    i+=1
                
                if(ptr  == self.Tail):
                    self.Tail.Next = nd
                    nd.Prev = self.Tail
                    self.Tail = nd
                    self.size +=1
                else:
                    ptr.Next.Prev = nd
                    nd.Next = ptr.Next
                    ptr.Next = nd
                    nd.Prev = ptr 
                    self.size +=1

    def searchByName(self, name):
        nd = self.Head
        if (nd != None):
            while nd != None:
                if nd.Data.name == name.lower():
                    return nd
                elif nd == None:
                    return 0

                else:
                    nd = nd.Next
        else:
            return 0
    
    def deleteById(self, id):
        nd = None
        if self.Head != None:
            nd = self.Head
          
            if nd.Data.id == id:
                            self.Head = self.Head.Next
                            self.Head.Prev = None
                            self.size -=1
                            return 1             
        
            else:
                nd = nd.Next
                while nd != None:
                   
                    if nd.Data.id == id:
                        if(self.Tail == nd):
                            self.Tail = self.Tail.Prev
                            self.Tail.Next = None
                            self.size -=1
                            return 1

                        else:  
                            nd.Prev.Next = nd.Next
                            nd.Next.Prev = nd.Prev 
                            self.size -=1
                            return 1
                   
                    nd = nd.Next
                    
 
        else:
            return 0


    def deleteAllByGroup(self, group):
        nd = None
        if self.Head != None:
            nd = self.Head
            while nd != None:
                if nd.Data.group == group:
                            self.Head = self.Head.Next
                            self.Head.Prev = None
                            self.size -=1
                            nd = nd.Next 
                
                else:
                    while nd != None:
                        if nd.Data.group == group:
                            if(self.Tail == nd):
                                self.Tail = self.Tail.Prev
                                self.Tail.Next = None
                                self.size -=1
                            else:  
                                nd.Prev.Next = nd.Next
                                nd.Next.Prev = nd.Prev 
                                self.size -=1
                        nd = nd.Next
                
                    
        else:
            return 0

    def deleteAll(self):
        self.Head = self.Tail = None
        self.size = 0


    def displayAll(self):
        nd = self.Head
        i = 0
        while i <  self.size:
            print(nd)
            nd = nd.Next
            i+=1
        







