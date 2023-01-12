id_list = [1, 2, 3, 4]
name_list = ["ahmed ali", "Ali ahmed", 'amr ahmed', 'ali mahmoud']
sal_list = [2000, 3000, 4000, 5000]
dep_list = ['finance', 'HR','Eng','HR']

while True:
    print(
        """
        1 - New
        2 - Search
        3 - Delete
        4 - Show All
        5 - Quite 
        """)
    choose = int (input('Enter Your Choose: '))
    match choose :
        case 1:
            id_list.append(id_list[-1]+1)
            new_std = input('Enter Your Name, Salary, Dep: ')
            name = new_std.split(',')[0].strip()
            name_list.append(name)

            salary = float(new_std.split(',')[1].strip() or 0.0) 
            sal_list.append(salary)

            dep = new_std.split(',')[2].strip()
            dep_list.append(dep)

            print('Added new Employee\nID: {} , Name: {} , Saralry {} , Departement {}'.format(id_list[-1], name_list[-1], sal_list[-1], dep_list[-1] ))
        
        case 2:
            search = input("Search by any char in frist name: ")
            for i , v in enumerate(name_list):
                if v.lower().startswith(search.lower()):
                      print('ID: {} , Name: {} , Saralry {} , Departement {}'.format(id_list[i], name_list[i], sal_list[i], dep_list[i] ))
        case 3:
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

        case 4:
            for i in range(len(name_list)):
                print('ID: {} , Name: {} , Saralry {} , Departement {}'.format(id_list[i], name_list[i], sal_list[i], dep_list[i] ))
        case 5:
            print('Bye')
            break





