class Coffeeshop:
    def __init__(self):
        self.total = 0                                 #initialize total 0
        self.item_prices={                             #create dictionary
            1: 100,
            2: 150,
            3: 200,
            4: 250,
            5: 80,
            6: 60,
            7: 120,
            8: 150
        }

    def display_welcome_message(self):                                    #Method to display message
        print("\t\t\t\t\t****************************************")
        print("\t\t\t\t\t*                 Welcome              *")
        print("\t\t\t\t\t*                    To                *")
        print("\t\t\t\t\t*                    UMT               *")
        print("\t\t\t\t\t*                 Coffee Shop          *")
        print("\t\t\t\t\t****************************************\n")    
              
    def displaymenu(self):                                                #Method to display menu
        print("\t\t\t\t\tMenu---")
        print("\t\t\t\t\t\t1. Espresso - Rs.100")
        print("\t\t\t\t\t\t2. Cappuccino - Rs.150")
        print("\t\t\t\t\t\t3. Latte - Rs.200")
        print("\t\t\t\t\t\t4. Mocha - Rs.250")
        print("\t\t\t\t\t\t5. Black Coffee - Rs.80")
        print("\t\t\t\t\t\t6. Tea - Rs.60")
        print("\t\t\t\t\t\t7. Chocolate Cake - Rs.120")
        print("\t\t\t\t\t\t8. CheeseCake - Rs.150\n")

    def calculatetotal(self,item,quantity):                              #Method to calculate total
        return item * quantity
    
    def takeorder(self):                                                   #Method to take order
        try:
            choice=int(input("\t\t\t\t\tEnter Your Choice:"))
            
            if(choice not in self.item_prices):
                print("\t\t\t\t\tInvalid Input")
                return
            
            quantity=int(input("\t\t\t\t\tEnter Quantity of Item:"))
            self.total+=self.calculatetotal(self.item_prices[choice],quantity)

            print(f"\t\t\t\t\tTotal Price is {self.total}")

        except ValueError:
            print("Invalid Input")    


def main():
    shop=Coffeeshop()                                      #create object

    shop.display_welcome_message()
    
    while True:                                           #loop for calling methods
        choice=int(input("\t\t\t\t\tEnter 1 to display menu:"))
        
        if(choice!=1):
            print("\t\t\t\t\tInvalid Input")

        else:
            shop.displaymenu()
            shop.takeorder()

            print("\t\t\t\t\t1:Menu")
            print("\t\t\t\t\t2:Exit")

            next_choice=int(input("\t\t\t\t\tEnter Your Choice:"))

            if(next_choice==2):
                print("\t\t\t\t\tSuccessfully Exit")
                exit(0)

            elif(next_choice!=1):
                print("\t\t\t\t\tInvalid Input") 
    
       
            
if __name__ == "__main__":
	main()

         


