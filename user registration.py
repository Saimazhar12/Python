import os

class User:
    def __init__(self,username,password):          #to set values
        self.username=username
        self.password=password

    def getusername(self):                         #to getusername
        return self.username

    def getpassword(self):                         #to getpassword
        return self.password
    
    def setusername(self,new_username):           #to set a new username
        self.username=new_username


class usermanager:
    def __init__(self):                            #create empty list
        self.userlist=[]

    def register_user(self):                       #Method to register user
        username=input("\t\tEnter Username:")  
        password=input("\t\tEnter Password:")  

        u1=User(username,password)

        self.userlist.append(u1)

        print("\t\t*User Register Successfully*")

    def login_user(self,name,passw):                #Method to login user
        for val in self.userlist:
            if(val.getusername()==name and val.getpassword()==passw):
                print("\t\t*Login Successfully*")   
                return True
             
         
        print("\t\t*Invalid Username or Password*")    
        return False


    def show_user_list(self):                        #Method to show user list
        print("\t\t---Users List---")
        for val in self.userlist:
            print(f"\t\t{val.getusername()}")
            


    def search_user(self,name):                     #Method to search user
        for val in self.userlist:
            if(val.getusername()==name):
                print("\t\t*User Found*")
                return
            
        print("\t\t*User not Found*")    

    def deluser(self,name):                         #Method to delete user
        for i,val in enumerate(self.userlist):
            if(val.getusername()==name):
                del self.userlist[i]   
                print("\t\t*User Delete successfully*")   
                return

        print("\t\t*User not found*")    
            

    def update_username(self, old_name, new_name):  # Method to update username
        for val in self.userlist:
            if(val.getusername() == old_name):
                val.setusername(new_name)
                print("\t\t*Username Updated Successfully*")
                return

        print("\t\t*User not found*")      


def main():
    um=usermanager()                    

    while True:
        os.system("cls")
        print("\n\n\t\t1:Register User")             
        print("\t\t2:Login User")
        print("\t\t3:Show User List")
        print("\t\t4:Search User")
        print("\t\t5:Delete User")
        print("\t\t6:Update Username") 
        print("\t\t7:Exit")


        choice=int(input("\t\tEnter Choice:"))

        if(choice==1):
            um.register_user()
            os.system("pause")


        elif(choice==2):
            username=input("\t\tEnter Username:")    
            password=input("\t\tEnter Password:")

            um.login_user(username,password)
            os.system("pause")

        elif(choice==3):
            um.show_user_list()
            os.system("pause")

        elif(choice==4):
            username=input("\t\tEnter Username:")  
            um.search_user(username)
            os.system("pause")

        elif(choice==5):
            username=input("\t\tEnter Username:") 
            um.deluser(username)
            os.system("pause")


        elif(choice==6):
            old_name=input("\t\tEnter Current Username: ")
            new_name=input("\t\tEnter New Username: ")
            um.update_username(old_name, new_name)
            os.system("pause")   
               


        elif(choice==7):
            exit(0)

        else:
            print("\t\tInvalid Choice") 
            os.system("pause") 
            


if __name__ == "__main__":
    main()






