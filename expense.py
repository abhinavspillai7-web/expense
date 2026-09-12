expense=[]
total=0
while True:
    print("1. add expense")
    print("2.veiw expense")
    print("3.total spending")
    print("4. exit")
    cho=int(input("enter choice:"))
    if cho ==1:
        user_agreed=True
        while user_agreed:
            dict1={}
            user=input("enter amt:")
            while not user.isdigit():
                print("Invalid amount")
                user = input("enter amt:")
            desp=input("enter discription:")
            while  desp.strip()== "":
                desp=input("enter discription:")
            categories = ["food", "travel", "shopping", "education", "other"]
            cat=input("enter category:")
            while cat.lower() not in categories:
                print("Invalid category")
                cat = input("enter category:")
            dict1["amount"]=user
            dict1["description"]=desp
            dict1["category"]=cat
            expense.append(dict1)
            total=int(dict1["amount"])+total
            inp=input("enter yes or no:")
            inp=inp.lower()
            if inp =="yes":
                user_agreed=True
            else:
                user_agreed=False
    elif cho == 2:
        print("-------expense---------")
        number=1
        for i in expense:
            for key, value in i.items():
                print(f"{number}:{key}:{value}")
            number=number+1
            print("-" *25)
        print("TOTAL:",total)
    elif cho==3:
        print("total spending")
        print("TOTAL:",total)
    elif cho==4:
        break
    else:
        print("invalid")