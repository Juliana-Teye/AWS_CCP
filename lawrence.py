print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("---------------1 will bring mtn------------------------")
print("---------------2 will be vodafone----------------------")
print("---------------0 to exit-------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
option = int(input("choose a bank"))
if (option == 1):
    print("MTN is the beast")
elif (option == 2):
    print("Vodafone: I hope you have tissues")
elif (option == 0):
    print("Thank you, See you ciaaoo")
    exit()
else:
    print("Invalid Response, Try Again")