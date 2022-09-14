num1=0
num_list=[]
while num1 != '':
    num1=input("enter numbers:")
    if num1 != '':
        num_list.append(int(num1))
num_list.sort(reverse= True)
print("the greatest numbers are :",num_list[0:5])

