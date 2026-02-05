import matplotlib.pyplot as mat
name=input("Enter your name:")
weight=float(input("Enter your weight in Kg:"))
height=float(input("Enter your height in centimeters:"))
height1=height/100
BMI=weight/(height1**2)
r=int(input("Enter the no. of rotis intake in a day:"))  
ri=int(input("Enter the amount of rice (1bowl=100g) intake in a day:"))
a=int(input("Enter the amount of arahar dal (1 bowl=100g) intake in a day:"))
e=int(input("Enter the no. of boiled eggs intake in a day:"))
c=int(input("Enter the amount of aloo curry intake in a day:"))
cu=int(input("Enter the amount of curd intake in a day:"))
p=int(input("Enter the no. of parathas intake in a day:"))
p1=p*150
r1=r*60
ri1=ri*130 
a1=a*220  
c1=c*105
cu1=cu*100  
e1=e*74   
total=r1+ri1+a1+c1+p1+cu1+e1
print("Hello",name)
print("Your BMI is:","{:.2f}".format(BMI))
print("Your total calories intake in a day is",total,"calories.") 
if (BMI<18.50):
    print("You are under weight.")
elif (18.50<BMI or BMI>24.90):
    print("You have healthy weight.")
elif (25.00<=BMI or BMI>29.90):
    print("You are overweight.")
else:
    print("You are obese.")   
n=2400
if n>total:
    print("You have to increase your calorie consumption by",n-total,"calories.")
else:
    print("You have to adjust your calorie intake.")        
if (BMI<18.50):
    print("You have Endomorph body type.")
elif (18.50<BMI or BMI>24.90):
    print("You have Mesomorph body type.")
else:
    print("You have Ectomorph body type.")     
calories=[p1,r1,ri1,a1,cu1,c1,e1] 
items=["parathas","rotis","rice","arahar dal","curd","aloo curry","eggs"]
mat.pie(calories,labels=items,autopct="%2.2f%%")
mat.show()
