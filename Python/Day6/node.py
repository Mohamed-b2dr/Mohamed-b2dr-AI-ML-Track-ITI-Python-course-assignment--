class Node:
    def __init__(self, data):
        self.Data =data
        self.Next= None
        self.Prev= None

    def __repr__(self) -> str:
         return f"(Node: (Data:{self.Data})"