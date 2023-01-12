import csv 
class Employe:
    employee_no = 0
    all =[]
    dep_dict ={}
    autoIncremented =0
    def __init__(self,name, salary, department) -> None:
        Employe.employee_no +=1
        self.id = Employe.employee_no 
        self.department = department
        self.__name = name
        self.__salary= salary
        Employe.all.append(self)
        Employe.dep_dict[department]= Employe.dep_dict.get(department,[])+[[self]]

    @property
    def name(self):
        return self.__name
    @property
    def salary(self):
        return self.__salary

    @name.setter
    def name(self, name):
        self.__name = name

    @salary.setter
    def salary(self, salary):
        if (salary > 0):
            self.__salary = salary
        else:
            print("Enter a valid salary Must be positive")


    def __repr__(self):
        return f"(Id: {self.id}, Name: {self.__name}, Salary: {self.__salary}, 'Departement:' {self.department})"

    @classmethod 
    def __scan(cls, new_std):
        name_list=[]
        name = new_std[0].strip()
        name_list.append(name)
        salary = float((new_std)[1].strip() or 0 )
        name_list.append(salary)
        dep = new_std[2].strip()
        name_list.append(dep)
        return name_list

    @classmethod 
    def __importfile(cls, path):
                try:
                    with open(path, 'r') as f:
                        lines = list(csv.DictReader(f))
                        for line in lines:
                            cls(**line)
                           
                except:
                    print('Enter a valid File')
               

    @classmethod 
    def newEmploye(cls, file = 0):
          
            if file == 0:
                new_std = input('Enter Your Name, Salary, Dep: ')
                try:
                    Employe(*cls.__scan(new_std.split(',')))
                    print('Added new Employee\n',cls.all[-1])
                except:
                    print("Enter Emplye with this format Name, Salay, Departement")
            
            else:
                cls.__importfile(file)
             
    @classmethod    
    def exportdepartement(cls):
            with open('departement.txt','w') as f:
                    for dep in  Employe.dep_dict:
                        f.write(dep+'\n')
                        for i in range (len(Employe.dep_dict[dep])):
                            f.write (str(cls.dep_dict[dep][i]) +'\n')
                        f.write('\n\n')                   
    @classmethod 
    def export(cls):
        with open('employe.txt','w') as f:
            for i in range(len(cls.all)):
                f.write (str(cls.all[i])+'\n')
    @classmethod 
    def search(cls):
                result =[]
                search = input("Search by any char in frist name: " ).strip() or '  '
                for i , v in enumerate(Employe.all):
                    if (v.name.lower().startswith(search.lower())):
                        print(cls.all[i])
                        result.append(Employe.all[i])
                return result
    @classmethod
    def delete(cls):
        result = cls.search()
        for i in result:
            cls.all.remove(i) 
        
    @classmethod
    def filter(cls, **kargs):

            for i , v in enumerate(Employe.all):
                if (kargs.get('name','') and kargs.get('salary',0) and  kargs.get('department','')):
                    if v.name == kargs.get('name') and v.salary == kargs.get('salary') and v.department == kargs.get('department'):
                            print(cls.all[i]) 
                elif(kargs.get('name','') and kargs.get('salary',0)):
                    if  (v.name == kargs.get('name') and v.salary == kargs.get('salary')) :
                            print(cls.all[i]) 

                elif (kargs.get('salary',0)and  kargs.get('department','')):
                    if (v.salary == kargs.get('salary')and v.department == kargs.get('department')):
                            print(cls.all[i]) 

                elif( kargs.get('name','') and kargs.get('department','')):
                    if (v.name == kargs.get('name') and  v.department == kargs.get('department')):
                            print(cls.all[i]) 

                elif( kargs.get('name',[]) or  kargs.get('salary',0) or  kargs.get('department',[])):
                    if (v.name == kargs.get('name') or v.salary == kargs.get('salary') or v.department == kargs.get('department')):
                            print(cls.all[i]) 


                        

       
        
            
    @classmethod
    def showAll(cls):
                     for i in range(len(cls.all)):
                        print(cls.all[i])



def printScreen(lst):
    for i in range(len(lst)):
        print(i, lst[i])


lst = ['Import','New','Search','Delete','Show All','Export ','Export Departement','Exit']
i =1
while i:
        printScreen(lst)
        choose = int (input('Enter Your Choose: '))
        match choose :
            case 0 :
                Employe.newEmploye('emps_in.csv')
            case 1:
                Employe.newEmploye()
            case 2:
                Employe.search()
            case 3:
                Employe.delete()
            case 4:
                Employe.showAll()
            case 5:
                Employe.export()
            case 6:
               Employe.exportdepartement()
            case 7:
                Employe.filter(name ='Ali', department = 'FIN')
                i-=1
                

