# obj = open("abc.txt","a")
# obj.write("This is the first line\n")
# obj.write("This is the sceond line\n")
# obj.write("This is the third line\n")
# obj.write("This is the four line\n")
# obj.close()

# f = open("abc.txt","r")
# for line in f:
#     if "three" in line :
#         print("This is the third line")
#     else:
#         print(line)
# f.close()

# f = open("abc.txt","a")
# f.write("This is the 7 line!\n")
# f.close()

f = open("abc.txt","w+")
# print(f.read())
# f.write("new line!\n")
# print("data:",f.read())
f.close()