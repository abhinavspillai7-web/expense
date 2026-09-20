import sqlite3
conn=sqlite3.connect("expenses.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY,
amount REAL,
description TEXT,
category TEXT)""")
conn.commit()
categories = ["food", "travel", "shopping", "education", "other"]      
while True:
    print("\n" + "=" * 40)
    print("          EXPENSE TRACKER")
    print("=" * 40)
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
            user=input("enter amt:")
            while not user.replace(".","",1).isdigit():
                print("Invalid amount")
                user = input("enter amt:")
            user=float(user)
            desp=input("enter discription:")
            while  desp.strip()== "":
                desp=input("enter discription:")
            cat=input("enter category:")
            while cat.lower() not in categories:
                print("Invalid category")
                cat = input("enter category:")
            cursor.execute("""
            INSERT INTO expenses (amount, description, category)
            VALUES (?, ?, ?)
            """, (user, desp, cat))
            conn.commit()
            inp=input("enter yes or no:")
            inp=inp.lower()
            if inp =="yes":
                user_agreed=True
            else:
                user_agreed=False
    elif cho == 2:
        print("\n" + "=" * 55)
        print("                  EXPENSES")
        print("=" * 55)
        print(f"{'No.':<5}{'Amount':<12}{'Description':<20}{'Category'}")
        print("-" * 55)
        number=1
        cursor.execute("SELECT * FROM expenses")
        items = cursor.fetchall()
        for i in items:
            print(f"{number:<5}₹{i[1]:<11.2f}{i[2]:<20}{i[3].title()}")
            number=number+1
            print("-"*25)
        cursor.execute("SELECT SUM(amount) FROM expenses")
        result=cursor.fetchone()
        print("-" * 55)
        print(f"{'TOTAL SPENDING':<38}₹{result[0] or 0:.2f}")
        print("=" * 55)
    elif cho==3:
        cursor.execute("SELECT SUM(amount) FROM expenses")
        result=cursor.fetchone()
        print("\n" + "=" * 40)
        print("             TOTAL SPENDING")
        print("=" * 40)
        print(f"        ₹{result[0] or 0:.2f}")
        print("=" * 40)
    elif cho==4:
        print("\n" + "=" * 45)
        print("             CATEGORY-WISE SPENDING")
        print("=" * 45)
        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        result=cursor.fetchall()
        for i in result:
            print(f"{i[0].title():<20}₹{i[1]:.2f}")
        print("-" * 45)
    elif cho==5:
        print("\n" + "=" * 55)
        print("                  EXPENSES")
        print("=" * 55)
        print("1. search by category")
        print("2.search by description")
        chose=int(input("enter choice:"))
        if chose==1:
            ask_cat=input("enter a category(food,travel,shopping,education,others):")
            ask_cat=ask_cat.lower()
            found=0
            result=cursor.execute("SELECT * FROM expenses WHERE category = ?", (ask_cat,))
            for i in result:
                print(f"₹{i[1]} | {i[2]} | {i[3].title()}")
                found=1
            if found == 0:
                print("not found")
        elif chose==2:
            ask_desc=input("enter your description:")
            ask_desc=ask_desc.lower()
            result=cursor.execute("SELECT * FROM expenses WHERE description = ?", (ask_desc,))
            found=0
            for i in result:
                    print(f"₹{i[1]} | {i[2]} | {i[3].title()}")
                    found=1
            if found == 0:
                print("not found")
        else:
            print("invalid")
    elif cho==6:
        print("\n" + "=" * 55)
        print("                  DELETE EXPENSE")
        print("=" * 55)
        num1=1
        cursor.execute("select * from expenses")
        result=cursor.fetchall()
        for i in result:
            print(f"{num1}:{i}")
            num1+=1
        if len(result)==0:
            print("no expense is currently present")
        else:
            num=int(input("enter your choice:"))
            index=num-1
            if num>=1 and num<=len(result):
                cursor.execute("delete from expenses where id =?",(result[index][0],))
                conn.commit()
                print(f"item deleted:{result[index]}")
            else:
                print("item not found")
    elif cho == 7:
        print("\n" + "=" * 55)
        print("                   EDIT EXPENSE")
        print("=" * 55)
        print("what do you want to edit")
        print("1.amount")
        print("2.description")
        print("3.category")
        choed = int(input("enter your choice:"))
        cursor.execute("select * from expenses")
        result = cursor.fetchall()
        if choed == 1:
            num3 = 1
            for i in result:
                print(f"{num3}.{i}")
                num3 = num3 + 1
            num2 = int(input("enter your choice:"))
            index1 = num2 - 1
            if num2 >= 1 and num2 <= len(result):
                new_amt = input("enter amt:")
                while not new_amt.replace(".", "", 1).isdigit():
                    print("Invalid amount")
                    new_amt = input("enter amt:")
                new_amt = float(new_amt)
                cursor.execute("update expenses set amount=? where id=?", (new_amt, result[index1][0]))
                conn.commit()
                print("edited sucessfully")
            else:
                print("item not found")
        elif choed == 2:
            num4 = 1
            for i in result:
                print(f"{num4}.{i}")
                num4 = num4 + 1
            num5 = int(input("enter your choice:"))
            index3 = num5 - 1
            if num5 >= 1 and num5 <= len(result):
                new_desc = input("enter new description:")
                while new_desc.strip() == "":
                    print("Invalid description")
                    new_desc = input("enter new description:")
                cursor.execute("update expenses set description=? where id=?", (new_desc, result[index3][0]))
                conn.commit()
                print("edited sucessfully")
            else:
                print("invalid number")
        elif choed == 3:
            num6 = 1
            for i in result:
                print(f"{num6}.{i}")
                num6 = num6 + 1
            num7 = int(input("enter your choice:"))
            index4 = num7 - 1
            if num7 >= 1 and num7 <= len(result):
                new_cat = input("enter new category:")
                new_cat = new_cat.lower()
                while new_cat not in categories:
                    print("invalid category")
                    new_cat = input("enter new category:")
                    new_cat = new_cat.lower()
                cursor.execute("update expenses set category=? where id=?", (new_cat, result[index4][0]))
                conn.commit()
                print("edited sucessfully")
            else:
                print("invalid")
        else:
            print("invalid number")
    elif cho==8:
        print("\n" + "=" * 40)
        print("          EXPENSE TRACKER")
        print("=" * 40)
        print("       Thank you for using")
        print("          Expense Tracker!")
        print("=" * 40)
        break
    else:
        print("invalid")