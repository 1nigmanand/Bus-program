number_of_people = int(input("enter the number_of_people\n-:"))
number_of_busses = int(input("enter the number_of_busses\n-:"))
list1 = []
list2 = []
def do_allocation(number_of_people,number_of_busses):
        a = 0
        b = 1
        c = 0
        val = number_of_people
        for i in range(number_of_busses):
                if val >=0:
                        list1.append(c)
                        a = b 
                        b = c
                        c = a+b
                        val-=c
                        list2.append(val)
                        
                elif list2[-1] == val:
                        list1.append(list2[-2])
                        list2[-1] = 10000
                else:
                        list1.append(0)
        val = val + c
        
        
        if list1[-2]>list1[-1]  and  list1[-1] != 0:
                return list1
            
        elif list1[-1] != 0:
                people = (f"{val} people remaing on bus stop because bus is not sufficent")
                return list1 , people  
        else:
                return list1

                

index = do_allocation(number_of_people , number_of_busses)  
print(index)