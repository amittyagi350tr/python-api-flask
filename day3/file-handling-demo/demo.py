with open("output.txt", "w") as f1:
    #first 2 lines: manually data is being written
    f1.write("Hello\n")
    f1.write("This is line2\n")
    data=["sample line 3\n", "sample line 4\n"]

    #we are copying data from a list in python into the file
    f1.writelines(data) #file will get closed

print("Done with example!")
f1.readlines() #file is not accessible, so error!!!!


