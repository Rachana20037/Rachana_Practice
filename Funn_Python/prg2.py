# print("hello world")
# sum=0
# n=int(input("Enter the number :"))
# while n>0:
#     sum=sum+n
#     n-=1
#     print("sum : ",sum)
# print("Bye")


# pattern 1
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# pattern 2

# break statement
for letter in "python":
    if letter == "h":
        break
    print("current letter : ",letter)
print("bye")
    
# continue  statement
for letter in "python":
    if letter =="h":
        continue
    print("current letter :",letter)
    

# pass statement
for letter in "python":
    if letter =="h":
        pass
        print("pass block")
    print("current letter :",letter)