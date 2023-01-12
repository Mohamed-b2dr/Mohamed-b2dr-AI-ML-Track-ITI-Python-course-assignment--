import csv 
#csv.DictReader(f)
class Student:
  
     student_no = 0
     all = []
     def __init__(self, name, age, height):
        self.name = name
        self.age = int(age)
        self.height = int(height)
        Student.student_no +=1
        Student.all.append(self)

     def __str__(self):
        return f"name: {self.name}, age: {self.age}"

     def __repr__(self):
        return f"(name: {self.name}, age: {self.age},Height: {self.height})"

     def __len__(self):
        return self.height

     def attend(self):
        if self.height > 160:
            return "present"
        else:
            return "absent"
     def attend(self, n):
   
     @classmethod
     def CreateFromName(cls, name):
         return cls(name, 0,0)

     @classmethod
     def Import_file(cls, path):
        with open(path, 'r') as f:
            lines = list(csv.DictReader(f))
        for line in lines:
            cls(**line)
        """with open(path, 'r') as f:
            data = f.read().split('\n')
        for line in data[1:]:
            cls(*line.split(','))"""
     @classmethod
     def fliterName(cls, filter_name):
        return list(filter(lambda x : x.name.lower() == filter_name.lower(), cls.all))
     @classmethod
     def fliterAge(cls, filter_age):
        return list(filter(lambda x : x.age == filter_age, cls.all))
     @classmethod
     def fliterStartname(cls, filter_name):
        return list(filter(lambda x :  x.name.lower().startswith(filter_name.lower())  , cls.all))
     @classmethod
     def deleteByName(cls, filter_name):
         result = Student.fliterName(filter_name)
         for item in result:
            cls.all.remove(item)

     
        
    
    


if __name__ == '__main__':

    Student.Import_file('stds_in.csv')
    print(Student.all[0])
    print(Student.fliterName('Muhammed'))
    print(Student.fliterAge(filter_age =27))
    print(Student.fliterStartname('H'))
    Student.deleteByName('Muhammed')
    print(Student.all)
    s = Student('M', 10,10)
    s.attend()



  
    

    #print(s)
    #print(len(s))































