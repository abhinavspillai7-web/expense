expense=[]
total=0
while True:
    print("1. add expense")
    print("2.veiw expense")
    print("3.total spending")
    print("4. categorise spending")
    print("5.search and filter")
    print("6.exit")
    cho=int(input("enter choice:"))
    if cho ==1:
        user_agreed=True
        while user_agreed:
            dict1={}
            user=input("enter amt:")
            while not user.replace(".","",1).isdigit():
                print("Invalid amount")
                user = input("enter amt:")
            user=float(user)
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
        category_total = {"food": 0,"travel": 0,"shopping": 0,"education": 0,"other": 0}
        for i in expense:
            category_total[i["category"]] = category_total[i["category"]] + i["amount"]
        for i in category_total:
           print(f"{i.title()}:${category_total[i]:.2f}")
    elif cho==5:
        ask_cat=input("enter a category(food,travel,shopping,education,others):")
        ask_cat=ask_cat.lower()
        found=0
        for i in expense:
            if  ask_cat == i["category"]:
                print("found")
                print(f"₹{i['amount']} | {i['description']} | {i['category'].title()}")
                found=1
        if found == 0:
            print("not found")

    elif cho==6:
        break
    else:
        print("invalid")