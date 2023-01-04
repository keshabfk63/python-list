print("welcome")
msg="press 1 if you want to continue operation otherwise enter any other key:"
menu=1



while(menu==1):
    work=int(input("enter 1 for create,2 for add,3 for remove,4 for delete, 5 for pop,6 for clear:"))
    if work==1:
        fruits=list(map(str,input("enter data for list:").split()))
        print(fruits)
        menu=int(input(msg))
    
    elif work==2:
        fruits=[]
        new=input("enter new data to add in list:")
        fruits.append(new)
        print(fruits)
        new_item=int(input("enter in which index you want to add new item:"))
        new1=input("enter new data to add in list:")
        fruits.insert(new_item,m=new1)
        print(fruits)
        menu=int(input(msg))
    
    elif work==3:
        fruits=["Apple","Banana","Mango","Papaya","Grapes","Orange"]
        print(fruits)
        remove1=input("enter which item do you want to remove:")
        fruits.remove(remove1)
        print(fruits)
        menu=int(input(msg))
    
    elif work==4:
        fruits=["Apple","Banana","Mango","Papaya","Grapes","Orange"]
        print(fruits)
        index_of_item=int(input("enter the index of item you want to delete:"))
        del fruits[index_of_item]
        print(fruits)
        menu=int(input(msg))

    elif work==5:
        fruits=["Apple","Banana","Mango","Papaya","Grapes","Orange"]
        print(fruits)
        print("After pop operation the following output is generated:")
        fruits.pop()
        print(fruits)
        menu=int(input(msg))
    
    elif work==6:
        fruits=["Apple","Banana","Mango","Papaya","Grapes","Orange"]
        print(fruits)
        fruits.clear()
        print(fruits)
        menu=int(input(msg))
    

    else:
        print("wrong input")
        menu=int(input(msg))

