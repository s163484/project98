def swapFileData():
    print("swapping files")
    fileName1 = input("enter file1 name")
    file1 = open(fileName1,"r+")
    
    print(file1.read())

   #storing and writing to file NOT working
    storeFile1 = file1.read()
    

    fileName2 = input("enter file2 name")
    file2 = open(fileName2,"w+")

#write operation  
    file2.write(file1.read())

    print("file2 contents " + file2.read())
     
 
    file1.close()
    file2.close()
    

swapFileData()
