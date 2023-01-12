id_list = []
name_list = []
sal_list = []
dep_list = []

def addEmploye(new_std):
            id_list.append(new_std.split(',')[0].strip())
            name = new_std.split(',')[1].strip()
            name_list.append(name)
            salary = float(new_std.split(',')[2].strip() or 0.0) 
            sal_list.append(salary)
            dep = new_std.split(',')[3].strip()
            dep_list.append(dep)
def newEmploye():
            id_list.append(len(id_list)+1)
            new_std = input('Enter Your Name, Salary, Dep: ')
            name = new_std.split(',')[0].strip()
            name_list.append(name)
            salary = float(new_std.split(',')[1].strip() or 0 )

            dep = new_std.split(',')[2].strip()
            dep_list.append(dep)

            print('Added new Employee\nID: {} , Name: {} , Saralry {} , Departement {}'.format(id_list[-1], name_list[-1], sal_list[-1], dep_list[-1] ))

def delete():
            delete = input("Delete person with name: ")
            i = 0
            while (i < len(id_list) ):
                    if name_list[i].lower().startswith(delete.lower()):
                            id_list.pop(i)
                            name_list.pop(i)
                            sal_list.pop(i)
                            dep_list.pop(i)
                      
                    else:
                        i+=1

def search():
            search = input("Search by any char in frist name: ")
            for i , v in enumerate(name_list):
                if v.lower().startswith(search.lower()):
                      print('ID: {} , Name: {} , Saralry {} , Departement {}'.format(id_list[i], name_list[i], sal_list[i], dep_list[i] ))
                      
def export():
     with open('employe.txt','w') as f:
        for i in range(len(id_list)):
            f.write ('ID: {} , Name: {} , Saralry {} , Departement {} \n'.format(id_list[i], name_list[i], sal_list[i], dep_list[i] ))

def get_dictionary():
        departement = dict()
        for i, dep in enumerate(dep_list):
            departement.get(dep,[])+[[id_list[i], name_list[i], sal_list[i], dep_list[i]]]

def exportdepartement():
        departement =get_dictionary()
        with open('departement.txt','w') as f:
                for dep in departement:
                    f.write(dep+'\n')
                    for i in range (len(departement[dep])):
                        f.write ('ID: {} , Name: {} , Saralry {} , Departement {} \n'.format(departement[dep][i][0],departement[dep][i][1],departement[dep][i][2],departement[dep][i][3]))
                    f.write('\n\n')
                


while True:
    print(
        """
        0 - Import
        1 - New
        2 - Search
        3 - Delete
        4 - Show All
        5 - Export 
        6 - Export Departement
        7 - Exit
        """)
    choose = int (input('Enter Your Choose: '))
    match choose :
        case 0 :
            with open('emps_in.txt', 'r') as data:
                file = data.readlines()
                for f in file:
                    addEmploye(f)


        case 1:
             newEmploye()
        case 2:
             search()
        case 3:
             delete()
        case 4:
            for i in range(len(name_list)):
                print('ID: {} , Name: {} , Saralry {} , Departement {}'.format(id_list[i], name_list[i], sal_list[i], dep_list[i] ))
        case 5:
            export()
        case 6:
            exportdepartement()
        case 7:
            print('Bye')
            break




