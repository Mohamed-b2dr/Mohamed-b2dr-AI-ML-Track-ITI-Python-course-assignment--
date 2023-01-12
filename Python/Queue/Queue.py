class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, data):
        self.arr.append(data)

    def dequeue(self):
        if len(self.arr) > 0:
            x = self.arr[0]
            for i in range(len(self.arr)-1):
                        self.arr[i] = self.arr[i+1] 
            self.arr.pop()
            return  x
     

    def __repr__(self):
        return f"Queue({self.arr})"




if __name__ == '__main__':
    Q1 = Queue()
    Q1.enqueue(10)
    Q1.enqueue(24)
    print(Q1)
    print(Q1.dequeue())
    print(Q1)
    Q1.enqueue(3)
    print(Q1)