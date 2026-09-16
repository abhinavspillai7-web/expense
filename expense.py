import json
expense=[]
total=0
try:
    with open("expenses.json","r") as file:
        expense=json.load(file)
except FileNotFoundError:
    expense=[]       
while True:
    print("1. add expense")
    print("2.veiw expense")
    print("3.total spending")
    print("4. categorise spending")
    print("5.search and filter")
    print("6.delete expense")
    print("7.edit expense")
    print("8.exit")
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
            with open("expenses.json","w") as file:
                json.dump(expense,file)
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
        print("1. search by category")
        print("2.search by description")
        chose=int(input("enter choice:"))
        if chose==1:
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
        elif chose==2:
            ask_desc=input("enter your description:")
            ask_desc=ask_desc.lower()
            found=0
            for i in expense:
                if  ask_desc == i["description"]:
                    print("found")
                    print(f"₹{i['amount']} | {i['description']} | {i['category'].title()}")
                    found=1
            if found == 0:
                print("not found")
        else:
            print("invalid")
    elif cho==6:
        num1=1
        for i in expense:
            print(f"{num1}.{i}")
            num1=num1+1
        if len(expense)==0:
            print("no expense is currently present")
        else:
            num=int(input("enter your choice:"))
            index=num-1
            if num>=1 and num<=len(expense):
                deleted_item=expense.pop(index)
                with open("expenses.json","w") as file:
                    json.dump(expense,file)
                print(f"item deleted:{deleted_item}")
            else:
                print("item not found")
    elif cho == 7:
        print("what do you want to edit")
        print("1.amount")
        print("2.description")
        print("3.category")
        choed = int(input("enter your choice:"))
        if choed == 1:
            num3 = 1
            for i in expense:
                print(f"{num3}.{i}")
                num3 = num3 + 1
            num2 = int(input("enter your choice:"))
            index1 = num2 - 1
            if num2 >= 1 and num2 <= len(expense):
                new_amt = input("enter amt:")
                while not new_amt.replace(".", "", 1).isdigit():
                    print("Invalid amount")
                    new_amt = input("enter amt:")
                new_amt = float(new_amt)
                expense[index1]["amount"] = new_amt
                with open("expenses.json","w") as file:
                    json.dump(expense,file)
                print("edited sucessfully")
            else:
                print("item not found")
        elif choed == 2:
            num4 = 1
            for i in expense:
                print(f"{num4}.{i}")
                num4 = num4 + 1
            num5 = int(input("enter your choice:"))
            index3 = num5 - 1
            if num5 >= 1 and num5 <= len(expense):
                new_desc = input("enter new description:")
                while new_desc.strip() == "":
                    print("Invalid description")
                    new_desc = input("enter new description:")
                expense[index3]["description"] = new_desc
                with open("expenses.json","w") as file:
                    json.dump(expense,file)
                print("edited sucessfully")
            else:
                print("invalid number")
        elif choed == 3:
            num6 = 1
            for i in expense:
                print(f"{num6}.{i}")
                num6 = num6 + 1
            num7 = int(input("enter your choice:"))
            index4 = num7 - 1
            if num7 >= 1 and num7 <= len(expense):
                new_cat = input("enter new category:")
                new_cat = new_cat.lower()
                while new_cat not in categories:
                    print("invalid category")
                    new_cat = input("enter new category:")
                    new_cat = new_cat.lower()
                expense[index4]["category"] = new_cat
                with open("expenses.json","w") as file:
                    json.dump(expense,file)
                print("edited sucessfully")
            else:
                print("invalid")
        else:
            print("invalid number")
    elif cho==8:
        break
    else:
        print("invalid")