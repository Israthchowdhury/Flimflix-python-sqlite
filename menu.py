import readRecords, addRecords, updateRecords, deleteRecords
from time import sleep

def menuOptions():
    options = 0
 
    # check for the value 0 in the list
    while options not in ["1", "2", "3", "4", "5", "6"]:
        print("\nMenu Options")
        print("1. Add a Record")
        print("2. Delete a Record")
        print("3. Amend a Record")
        print("4. Print all Records")
        print("5. Report Menu Option ")
        print("6. Exit")
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5", "6"]:

             print("Not in the list of options available")
    return options


mainProgram = True

while mainProgram == True:
     mainMenu = menuOptions()
     if mainMenu == "1":
         addRecords.addRecords()
     elif mainMenu == "2":
        deleteRecords.deleteRecords()
     elif mainMenu == "3":
         updateRecords.updateRecords()
     elif mainMenu == "4":
         readRecords.readRecords()
     else:
            mainProgram = False
input("Press enter to exit")
sleep(1.5)
print("Press the run button to start the programme again")
sleep(1.5)
exit()