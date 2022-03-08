print("Hello, World")
print("Python has three numeric types: int, float, and complex")
myValue=1
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=3.14
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=True
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=False
print(str(myValue) + " is of the data type " + str(type(myValue)))
myString = "This is a string"
print(myString)
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdstring = firstString + secondString
print(thirdstring)
name = input("What is your name? ")
print(name)
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
myFruitList[2] = "orange"
print(myFruitList)
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    import csv
    import copy
    myVehicle = {
        "vin" : " ",
        "make" : " ",
        "model" : " ",
        "year" : 0,
        "range" : 0,
        "topSpeed" : 0,
        "zeroSixty" : 0.0,
        "mileage" : 0
        }
    for key, value in myVehicle.items():
        print("{} : {}".format(key,value)) 
    myInventoryList = []
    with open('car_fleet.csv') as csvFile:
        csvReader = csv.reader(csvFile,delimiter=',')
        lineCount = 0  
        for row in csvReader:
            if lineCount == 0:
               print(f'Column names are: {", ".join(row)}')  
               lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    currentVehicle = copy.deepcopy(myVehicle)
    for myCarProperties in myInventoryList:
      for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
        userReply = input("Do you need to ship a package? (Enter yes or no) ")
        if userReply == "yes":
            print("We can help you ship that package!")
        else:
            print("Please come back when you need to ship a package. Thank you")
            userReply = input("Would you like to buy stamps, buy an envelope, or make a copy (Enter stamps, envelope or copy) ")
            if userReply == "stamps":
                print("We have many stamp designs to choose from.")
            elif userReply == "envelope":
                print("We have many envelope sizes to choose from.")
            elif userReply == "copy":
                copies = input("How many copies would you like? (Enter a number) ")
                print("Here are {} copies.".format(copies))
            else:
                print("Thank you, please come again")
            
    
            
            
            
            
                