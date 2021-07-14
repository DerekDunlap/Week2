import os
os.system("clear")

shopping_lists=[]

#Shopping_List class
class ShoppingList:

    def __init__(self,title,address):
        #Initialize Shopping List accepts (title & address)
        self.title=title
        self.address=address
        self.grocery_items=[]

    def add_grocery_item(self):
        #add grocery item to a particular grocery list/store shopping list
        #Add item(s) to your Shopping List
        title=input("\nPlease enter the name of the item or Press 'q' to go back to Main Menu: ")
        price=float(input("Please enter the price of the item: $"))
        quantity=int(input("Please enter the quantity that you wish to purchase: "))
        item=GroceryItem(title,price,quantity)
        shopping_list.grocery_items.append(item)
        os.system("clear")
        

    def display_shopping_lists(self):
        os.system("clear")
        #display shopping list
        print("---------- My Shopping Lists ----------\n")
        for i in range(0,len(shopping_lists)):
            print(f"{i+1} - {shopping_lists[i].title} {shopping_lists[i].address}")
        print("\n")

    def display_shopping_list(self,number):
        os.system("clear")
        #display shopping list
        for i in range(0,len(shopping_lists)):
            if((number-1)==i):
                print(f"-------------------- {shopping_lists[i].title}'s Shopping List --------------------\n")
                for j in range(0,len(shopping_lists[i].grocery_items)):
                    print(f"{j+1} - {shopping_lists[i].grocery_items[j].title}    ${shopping_lists[i].grocery_items[j].price}    Quantity: {shopping_lists[i].grocery_items[j].quantity}")

class GroceryItem:
  def __init__(self,title,price,quantity):
    #name of item
    self.title=title
    self.price=price
    self.quantity=quantity
    

#Ask for user input

while(True):
    choice=input("Press 1 - Add a store to Shopping List:\nPress 2 - Delete store from Shopping List:\nPress 3 - View all stores on Shopping List:\nPress 4 - View a particular store's Grocery List:\nPress Q - Quit Program:\n\nEnter choice: ")
    if(choice=='1'):
        #Add a store to the Shopping List
        os.system("clear")
        title=input("Please enter store name: ")
        address=input("Please enter store address: ")
        shopping_list=ShoppingList(title, address)
        shopping_lists.append(shopping_list)
        
        #Provides user witht the option to add a new item to a store's shopping list
        shopping_list.add_grocery_item()
            
    elif(choice=='2'):
        #Delete from shopping_lists
        os.system("clear")
        shopping_list.display_shopping_lists()
        number=int(input("Enter the number of the store that you wish to delete: "))
        del shopping_lists[number-1]
        shopping_list.display_shopping_lists()

    elif(choice=='3'):
        #View all shopping lists
        shopping_list.display_shopping_lists()

    elif(choice=='4'):
        #Displays all shopping lists to allow user to input desired store's shopping list
        shopping_list.display_shopping_lists()
        number=int(input("Please enter the number of the Store that you wish to view: "))
        #View shopping list for a particular start (accepts number as a argument)
        while True:
            shopping_list.display_shopping_list(number)
            option=input("\n\nEnter 'A'- Add an item to this shopping list: \nEnter 'D'- To return to the Main Menu:\n\nEnter option: ")
            if(option=='A' or option=='a'):
                #Provides user witht the option to add a new item to a store's shopping list
                shopping_list.add_grocery_item()
            elif(option=='D' or option=='d'):
                os.system("clear")
                break

    elif(choice=='q' or choice=='Q'):
        #Quit Program
        os.system("clear")
        print("Ending the program...")
        print("3")
        print("2")
        print("1")
        print("Program terminated")
        break
