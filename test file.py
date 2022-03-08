var = open("file.txt", "r")

print(var.read())

var2 = open("file.txt", "r")
var2.write("this is what I am writing from the pthon file")

import json
import os

#print(os.listdir())
#os.mkdir("test folder")
#os.removedirs("test folder")

j_write = open("acc5.json", "w")
json.dump([1, "asas", 123, 323], j_write)

print(json.loads(j_write))