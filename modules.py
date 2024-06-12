import module_1

option = input("Which simulation would you like to run? \n 1. Matrix \n 2. Wii Sports \n")

if option.lower() == "matrix" or option == "1":
    module_1.main()
elif option.lower() == "wii sports" or option == "2":
    print("Running Wii Sports simulation...")
else:
    print("Invalid option selected.")
