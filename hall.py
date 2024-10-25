#1st number question requirement
class Star_cinema : 
    

    __hall_list = [] # create a class attribute 



    @classmethod
    def entry_hall(cls,hall_obj):
        cls.__hall_list.append(hall_obj) 

    @classmethod 
    def view_hall(cls):
        for hall in cls.__hall_list:
            print(f"Hall Number : {hall.get_hallNo()} , Row : {hall.get_rowNo()} , Col: {hall.getColNo()}")


class Hall(Star_cinema):

     #2nd number question requirement   
    def __init__(self , rows , cols , hall_no ) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}
        self.entry_hall(self)
        
        

    # 3 number question requirement
    def entry_show(self,id,movie_name , time):
        self.id = id 
        self.movie_name = movie_name 
        self.time = time
        info = (self.id, self.movie_name, self.time)
        self.__show_list.append(info)
        self.__seats[id] = []
        

        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append(0)
            self.__seats[id].append(row)

    # 4 number question Requirement
    def book_seat(self , id ):

        if not self.__seats:
            print(f"There Is No Show Currently Running.\n")
            return

        
        if id not in self.__seats : #check id is available in seats diction 
            print(f"Invalid Show Id \n\n")
            return

        NumberOfTicket = int(input('Numher Of Ticket?: '))


        availableTicket = 0 

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0: 
                    availableTicket+=1 
        
        if availableTicket < NumberOfTicket :
            print(f"There are not that many tickets for this show {id}.")
            return

        print(f"\nAvailable Seat for the show {id}")

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0:
                    print(f"Seat ({i} , {j}) --> Free")
                else:
                    print(f"Seat ({i} , {j}) --> Booked")
            

        print(f"\n\nUpdated Seats Layout : \n")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(self.__seats[id][i][j] ,end=" ")
            print("\n")

       
        for i in range(NumberOfTicket):
            while True: 
                SeatRow = int(input('Enter Seat Row: '))
                SeatCol = int(input("Enter Seat Column: "))

                if(SeatRow >= 0 and SeatRow < self.__rows) and (SeatCol >= 0 and SeatCol < self.__cols):
                    if self.__seats[id][SeatRow][SeatCol] == 0 :
                        self.__seats[id][SeatRow][SeatCol] = 1 
                        print(f"Seat {SeatRow} , {SeatCol} is Booked Successfully .")
                        break
                    else: 
                        print(f"This Seat {SeatRow}, {SeatCol} Already Booked . Please select Another Ones.\n")
                else:
                    print(f"Invalid Seat selection . Please select Valid Seat Row And Col\n")
                    

    #5 number question requirement
    def view_show_list(self):
        if len(self.__show_list) == 0:  #check show list is empty or not if check list is empty then return
            print(f"There Is No Show Currently Running.\n")
            return

        for value in self.__show_list: # Print each show in the show list
            print(value)
        print("\n")

    #6 number question requirement ( view_available_seats()  which will take an id of show, and view the seats that are available in that show	)
    def view_available_seats(self , id ):
        if not self.__seats:
            print(f"There Is No Show Currently Running.\n")
            return
        
        if id not in self.__seats: # it's complexity o(1)
            print(f"Invalid Show Id\n")
            return



        print(f'Available Seat for show  {id}')

        # rowSize = len(self.__seats[id]) # find the row size 
        # colSize = len(self.__seats[id][0])#find the col size

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0 :
                    print(f"seat ({i} , {j}) --> Free")
                else:
                    print(f"seat ({i} , {j}) --> Booked")
        
        print("\n")
        print(f"Updated Seats Layout : ")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(self.__seats[id][i][j], end= " ")
            print()


    
    #getter Method Use for access Private attribute
    def get_hallNo(self):
            return self.__hall_no
    
    def get_rowNo(self):
        return self.__rows

    def getColNo(self):
        return self.__cols
    
    def __repr__(self) -> str:
        return f"HallNumber : {self.__hall_no} Rows : {self.__rows} Cols : {self.__cols}"


HallDictionary = {}

while True:
    print("\n\t<------------------*********************---------------------->\n")
    print(f"\t\t\t\tWho are You ? ")
    print(f"\t\t\t\t1.Are You HallOwner/HallManager")
    print(f"\t\t\t\t2.Are You User")
    print(f"\t\t\t\t3.Exit")
    print("\n\t<------------------*********************---------------------->\n")
    option = int(input("Select Option : "))
    if option == 1 :
        while True: 
            print("\n\t\t<------------------*********************---------------------->\n")
            print(f"\t\t\t\t1.Are You want a create a new Hall in your Star cinema")
            print(f"\t\t\t\t2.Are You want to entry show")
            print(f"\t\t\t\t3.Show All the Halls in Star Cinema")
            print(f"\t\t\t\t4.Do You want to Back")
            print("\n\t\t<------------------*********************---------------------->\n")
            # print(f"1. Yes...")
            # print(f"2. No...")
            chose = int(input("Chose Your Option: "))

            if chose ==1 :

                rowss = int(input("\tHow many rows do you want? "))
                colss = int(input("\tHow many column do you want? "))
                hallNumber = int(input("\tEnter Hall Number "))
                print("\n\t\t<------------------*********************---------------------->\n")

                if hallNumber in HallDictionary:
                    print(f"\t\t\nThis hallNumber Hall already exist .Enter different HallNumber :\n\n")
                    continue

                HallDictionary[hallNumber] = Hall(rowss,colss,hallNumber)

                

            elif chose == 2 : 
                
                if not HallDictionary:
                    print(f"\t\t\nNo Halls Available. Please create One First\n\n")
                    continue

                print(f"\t\tExisted Hall List : \n\n")
                for key,value in HallDictionary.items():
                    print(f"HallNumber: {key} - {value}")
                print("\n")
                print("\n\t\t<------------------*********************---------------------->\n")


                HallNumber = int(input("\t\tEnter Hall_Number : "))
                if HallNumber not in HallDictionary:
                    print(f"\t\tHallNumber is not exist ")
                    continue
                
                print(f"\n\t\tRunning Show: \n")
                HallDictionary[HallNumber].view_show_list()
                print("\n")
                
                id = int(input("\t\t\tEnter Movie Id : "))
                MovieName = input("\t\t\tEnter Movie Name: ")
                Time = input("\t\t\tEnter show Time : ")
                HallDictionary[HallNumber].entry_show(id,MovieName,Time)
            
            elif chose == 3 : 
                if not HallDictionary:
                    print(f"\t\t\tNo Halls Available . please Create One First.\n")
                    continue
                Star_cinema.view_hall()

            else:
                break

    elif option == 2:
        
        
        if not HallDictionary:
            print(f"\t\t\tNo Halls Available. Please Contract Hall Manager/Hall Owner for create a Hall and Entry a Show For Your Enjoyment\n")
            continue

        print(f"\t\t\t\tExisted Hall List : \n\n")
        for key,value in HallDictionary.items():
            print(f"\t\t\t\t\tHallNumber: {key} - {value}")
        print("\n")

        print("\t\t\tWhich hall's information do you want to know? Enter The HallNumber : \n")
        hallNumber 
        while True:
            hallNumber = int(input("Hall Numbers: "))
            if hallNumber not in HallDictionary:
                print(f"Enter Valid Hall Number . this is not valid ")
            else:
                break
   
        while True:
            print("\n\t\t<------------------*********************---------------------->\n")

            print('\t\t\t1. VIEW ALL THE SHOW TODAY')
            print('\t\t\t2. VIEW AVAILABLE SEATS')
            print('\t\t\t3. BOOK TICKET')
            print('\t\t\t4. EXIT')
            option = int(input('ENTER OPTION: '))

            print("\n\t\t<------------------*********************---------------------->\n")


            if option == 1 :
                # print(f"Existed Hall List : ")
                # for key,value in HallDictionary.items:
                #     print(f"HallNumber: {key} - {value}")
                # print("\n")

                # print(f"Which Hall All The Show  Are You Want To See")
                # hallNumber = int(input("Hall Numbers: "))
                # if hallNumber not in HallDictionary:
                #     print(f"Enter Valid Hall Number . this is not valid ")
                #     continue

                print("\t\t\t\t________************************___________")

                HallDictionary[hallNumber].view_show_list()

                print("\t\t\t\t________**************************__________")


            elif option == 2:

                # print(f"Existed Hall List : ")
                # for key,value in HallDictionary.items:
                #     print(f"HallNumber: {key} - {value}")
                # print("\n")

                # print(f"Which hall's available tickets do you want to view?")

                # print(f"Which Hall All The Show  Are You Want To See")
                # hallNumber = int(input("Hall Numbers: "))
                # if hallNumber not in HallDictionary:
                #     print(f"Enter Valid Hall Number . this is not valid ")
                #     continue

                

                id = int(input("Enter Show Id : "))
                HallDictionary[hallNumber].view_available_seats(id)

            elif option == 3:
                id = int(input('Enter Show Id : '))
                HallDictionary[hallNumber].book_seat(id)
            else:
                break
    else:
        break
        






