my_list = [i ** 2 for i in range(1,12)]
#list generation
f= open("output.txt","r+")
for item in my_list:
    f.write(str(item)+"\n") #writing into the file
f.close()

#reading the file
my_file=open("output.txt","r")
print(my_file.read())
my_file.close()

#reading each line

my_file=open("output.txt","r")
print(my_file.readline())
print(my_file.readline())
my_file.close()