import random
# l=["1","2","3","4","5","6","7","8","9","0","@","#","&"]
# a="abcdefghijklmnopqrstuvwxyz"
# l1=list(a)
# for i in l1:
#     l.append(i)
# print(l) 
# b=a.upper()
# l2=list(b)
# for i in l2:
#     l.append(i)
# print(l)
# n=int(input("Enter the number of characters you want in your password:"))
# password=""
# while(n!=0):
#     passw=random.choice(l)
#     password=password + passw
#     n=n-1
# print(password)
# second method
l=["@","#","&","<",">","?"]
a="abcdefghijklmnopqrstuvwxyz"
l1=list(a)
b=a.upper()
l2=list(b)
l3=[]
password=""
for i in range(0,10):
    l3.append(str(i))
list=[l,l1,l2,l3]
try:
    n=int(input("Enter the number of characters you want in your password:"))
    while(n!=0):
        passw=random.choice(random.choice(list)) 
        password=password+passw 
        n=n-1
    print(password)
except Exception as e:
    print("Please enter a valid input type.")
