import json
from datetime import datetime

tables_arr=[]
pool_dict_arr=[]

class PoolTables:

    #Default construct to create PoolTable objects
    def __init__(self,table_num):
        self.table_num=table_num
        self.is_occupied=False
        self.start_time=None
        self.end_time=None
        self.play_time=None

    def display_pool_tables(self):
        for i in range(0,len(tables_arr)):
                print(f"Pool Table Number # {tables_arr[i].table_num}\n\n")
                print(f"Status of Table: {tables_arr[i].is_occupied}\n\n")
                print(f"Start Date/Time: {tables_arr[i].start_time}\n\n")
                print(f"End Date/Time: {tables_arr[i].end_time}\n\n")
                if(tables_arr[i].is_occupied==True):
                    current_time=""
                    while True:
                        current_time=datetime.now()
                        break
                    tables_arr[i].play_time=current_time-self.start_time
                print(f"Total Time Played: {tables_arr[i].play_time}\n\n")
        #input("")

    def checkout_pool_table(self,number):  
        tables_arr[number-1].is_occupied=True
        tables_arr[number-1].start_time=datetime.now()
        start=tables_arr[number-1].start_time
        self.write_json_file(number)
        print (f"Pool Table {tables_arr[number-1].table_num} was checked out @ {self.start_time}!")
      

    def checkin_pool_table(self,number):
        tables_arr[number-1].is_occupied=False
        tables_arr[number-1].end_time=datetime.now()
        tables_arr[number-1].play_time=datetime.now()
        self.write_json_file(number)
        #start_time=datetime.strptime(tables_arr[number-1].start_time,'%H:%M:%S')
        
        #return self.end_time


    def display_occupied_tables(self):
        print("Checked Out Pool Tables")
        print("------------------------------")
        for i in range(0,len(tables_arr)):
            if(tables_arr[i].is_occupied == True):
                print(f"{i+1} - Pool table # {tables_arr[i].table_num} \n")
                print(f"Status of Table: {tables_arr[i].is_occupied}\n")
                print(f"Start Date/Time: {self.start_time}")
                while True:
                    tables_arr[i].play_time=datetime.now()
                    break
                start_time=datetime.strptime(tables_arr[i].start_time,'%H:%M:%S')
                tables_arr[i].play_time=tables_arr[i].play_time-start_time
                print(f"Total Time Played: {tables_arr[i].play_time}")
                print("******************************")
            else:
                continue

    def display_vacant_tables(self):
      print("Avaible Pool Tables")
      print("------------------------------")
      for i in range(0,len(tables_arr)):
        if(tables_arr[i].is_occupied == False):
            print(f"{i+1} - Pool table # {tables_arr[i].table_num}\n")
            print(f"Status of Table: {tables_arr[i].is_occupied}\n")
            print(f"Start Date/Time: {tables_arr[i].start_time}")
            print("******************************")
        else:
          continue

    def dict_to_pool_table(dict):
        return PoolTables(dict["table_number"])

    def write_json_file(self,number):
        if(tables_arr[number-1].is_occupied==True):
            start=tables_arr[number-1].start_time.strftime("%H:%M:%S")
            tables_arr[number-1].start_time=start
            pool_dict_arr.append(tables_arr[number-1].__dict__)
        else:
            end=tables_arr[number-1].end_time.strftime("%H:%M:%S")
            play=tables_arr[number-1].play_time.strftime("%H:%M:%S")
            tables_arr[number-1].end_time=end
            tables_arr[number-1].play_time=play
            pool_dict_arr.append(tables_arr[number-1].__dict__)
        with open("07-16-2021.json","w") as file:                     
            json.dump(pool_dict_arr,file)
    
    def read_json_file(self):

        with open("07-16-2021.json") as file:
            pool_dict_arr=json.load(file)

        new_dict_arr=self.dict_to_pool_table(pool_dict_arr)
        for pool_table in new_dict_arr:
            print(pool_table)

#Creates 12 Pool Table objects
for i in range(1,13):
  pool_table=PoolTables(i)
  tables_arr.append(pool_table)

#Print statement that displays all pool tables
#pool_table.display_pool_tables()
while True:
    #try:
        option=int(input("\n\n--------------Main Menu--------------\nOption 1. Check-out Pool Table:\nOption 2. Check-in Pool Table:\nOption 3. Display all tables: \nOption 0. Turn off Program:\n\nEnter option choice: "))
        if(option==1):
            pool_table.display_vacant_tables()
            #try:
            num=int(input("\nEnter the number of the table you want to Check-Out: "))
            if(tables_arr[num-1].is_occupied):
                print(f"\nERROR: POOL TABLE # {num} IS ALREADY CHECKED-OUT! RETURNING TO MAIN MENU...")
            else:
                    #Testing Purposes Only
                print(pool_table.checkout_pool_table(num))
            #except ValueError:
                #print("INVALID ENTRY - INPUT NUMBERS ONLY!")
        elif(option==2):
            pool_table.display_occupied_tables()
            #try:
            num=int(input("\nEnter the number of the table you want to Check-In: "))
            if(tables_arr[num-1].is_occupied):
                print(pool_table.checkin_pool_table(num))
            else:
                print(f"\nERROR: POOL TABLE # {num} IS ALREADY CHECKED-IN! RETURNING TO MAIN MENU...")
            #except ValueError:
            #    print("INVALID ENTRY - INPUT NUMBERS ONLY!")
        elif(option==3):
            pool_table.display_pool_tables()
        elif(option==0):
            print("Turning off")
            break
    #except ValueError:
        #print("Invalid entry: Only numbers are allowed!")
        #continue