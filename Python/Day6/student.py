class Student:
    def __init__(self, Id, Name, Group) -> None:
        self.id = Id
        self.name = Name
        self.group = Group


    def __repr__(self) -> str:
        return f"(Student: (ID:{self.id}, NAME: {self.name}, GROUP: {self.group})"