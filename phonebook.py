mydictionary = {"Juls":"0549420327", 
"Earl":"05554444222", 
"Luis":"0244888993" }
newcontact = input("Enter your name")
newdigits = input("Enter your digits")
mydictionary[newcontact] = newdigits 
print(mydictionary)

# Display contents of dictionary
mydictionary = {"Juls":"0549420327", 
"Earl":"05554444222", 
"Luis":"0244888993" }
# print(mydictionary)
# print(len(mydictionary))
colour = ["red","blue","green"]
counter = 0
while counter < 3:
    print(colour[counter])
    counter +=1

while True :
    print("this script will not stop")

rgb = ["red" ,"blue" ,"green"]
for color in rgb :
    print("current color is " + color)

    # Display contents of dictionary
contacts = {"Juls":"0549420327", 
"Earl":"05554444222", 
"Luis":"0244888993" }
for contact, phnum in contacts.items():
    print(contact + " has " +  phnum + " as his/her phone number")