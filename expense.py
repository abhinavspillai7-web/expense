expense=[]
user_agreed=True
while user_agreed:
    dict1={}
    user=int(input("enter amt:"))
    desp=input("enter discription:")
    cat=input("enter category:")
    dict1["amount"]=user
    dict1["description"]=desp
    dict1["category"]=cat
    print(dict1)
    expense.append(dict1)
    print(expense)
    inp=input("enter yes or no:")
    inp=inp.lower()
    if inp =="yes":
        user_agreed=True
    else:
        user_agreed=False
for i in expense:
    for key, value in i.items():
        print(f"{key}:{value}")
        print("-" *15)
