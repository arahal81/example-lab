
menu={"Appetizers":{"Wings":0,"Cookies":0,"Spring Rolls":0},
"Entrees":{"Salmon":0,"Steak":0,"Meat Tornado":0,"A Literal Garden":0},
"Desserts":{"Ice Cream":0,"Cake":0,"Pie":0},
"Drinks":{"Coffee":0,"Tea":0,"Unicorn Tears":0}};
print("""**************************************
**    Welcome to the Snakes Cafe!   **

**    Please see our menu below.    **

**

 ** To quit at any time, type "quit" **

**************************************""");
for i in menu:
    print(i);
    print("----------");
    for j in menu[i]:
        print(f"{j}\n");

print("""***********************************
** What would you like to order? **
***********************************
""");
while True:  
    user_input=input(">");
    is_exist=False
    if(user_input=="quit"):
        print("Your order is:")
        for i in menu:
            print(f"{i}\n----------");
        for j in menu[i]:
             if menu[i][j]!=0:
                print(f" ** {menu[i][j]} orders of {j}** ");
        break;
    for i in menu:
        for j in menu[i]:
            if j.upper()==user_input.upper():
                is_exist=True;
                menu[i][j]+=1;
                print(f" ** {menu[i][j]} orders of {user_input} have been added to your meal ** ");
    if not is_exist:
        print(" ** The item that you are choose it not exist in the menu please try agin! ** ");
