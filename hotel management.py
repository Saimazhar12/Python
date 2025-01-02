import os

class Room:
    def __init__(self,room_number,room_type):    #to set room details
        self.room_number=room_number
        self.room_type=room_type
        self.is_booked=False          #initialize the room is not booked

    def get_room_number(self):    #to get room number
        return self.room_number

    def get_room_type(self):    #to get room type
        return self.room_type

    def is_room_booked(self):    #to check if the room is booked
        return self.is_booked

    def book_room(self):    #to book the room
        self.is_booked=True

    def free_room(self):    #to free the room
        self.is_booked=False

    def set_room_type(self,new_type):  #to set a new room type
        self.room_type=new_type


class HotelManager:
    def __init__(self):       
        self.room_list=[]     #create an empty list of rooms

    def add_room(self):    #method to add a room
        room_number=input("\t\tEnter Room Number:")
        room_type=input("\t\tEnter Room Type (Single/Double/Suite):")

        room = Room(room_number, room_type)
        self.room_list.append(room)

        print("\t\t*Room Added Successfully*")

    def book_room(self,room_number):   #method to book a room
        for room in self.room_list:
            if(room.get_room_number()==room_number and not room.is_room_booked()):
                room.book_room()
                print("\t\t*Room Booked Successfully*")
                return

        print("\t\t*Room Not Available or Already Booked*")

    def show_room_list(self):    #method to show the list of rooms
        print("\t\t---Rooms List---")
        for room in self.room_list:
            if(room.is_room_booked()):
                status="Booked"
            else:
                status="Available"
            print(f"\t\tRoom {room.get_room_number()} - {room.get_room_type()} - {status}")

    def search_room(self,room_number):    #method to search for a room
        for room in self.room_list:
            if(room.get_room_number()==room_number):
                if(room.is_room_booked()):
                    status="Booked"
                else:
                    status="Available"                
                print(f"\t\tRoom Found: {room.get_room_number()} - {room.get_room_type()}- {status}")
                return

        print("\t\t*Room Not Found*")

    def delete_room(self,room_number):               #method to delete a room
        for i, room in enumerate(self.room_list):
            if room.get_room_number()==room_number:
                del self.room_list[i]
                print("\t\t*Room Deleted Successfully*")
                return

        print("\t\t*Room Not Found*")

    def update_room_type(self,room_number,new_type):    #method to update room type
        for room in self.room_list:
            if room.get_room_number()==room_number:
                room.set_room_type(new_type)
                print("\t\t*Room Type Updated Successfully*")
                return

        print("\t\t*Room Not Found*")


def main():
    hm = HotelManager()

    while True:
        os.system("cls")
        print("\n\n\t\t1:Add Room")
        print("\t\t2:Book Room")
        print("\t\t3:Show Room List")
        print("\t\t4:Search Room")
        print("\t\t5:Delete Room")
        print("\t\t6:Update Room Type")
        print("\t\t7:Exit")

        choice = int(input("\t\tEnter Choice:"))

        if(choice==1):
            hm.add_room()
            os.system("pause")

        elif(choice==2):
            room_number = input("\t\tEnter Room Number:")
            hm.book_room(room_number)
            os.system("pause")

        elif(choice==3):
            hm.show_room_list()
            os.system("pause")

        elif(choice==4):
            room_number = input("\t\tEnter Room Number:")
            hm.search_room(room_number)
            os.system("pause")

        elif(choice==5):
            room_number = input("\t\tEnter Room Number:")
            hm.delete_room(room_number)
            os.system("pause")

        elif(choice==6):
            room_number = input("\t\tEnter Room Number:")
            new_type = input("\t\tEnter New Room Type:")
            hm.update_room_type(room_number, new_type)
            os.system("pause")

        elif(choice==7):
            exit(0)

        else:
            print("\t\tInvalid Choice")
            os.system("pause")


if __name__ == "__main__":
    main()
