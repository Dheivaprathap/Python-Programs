print("10th mark sheet:")
m1=float(input("enter English m1:"))
m2=float(input("enter Tamil m2:"))
m3=float(input("enter Maths m3:"))
m4=float(input("enter science m4:"))
m5=float(input("enter social m5:"))
print("English m1 value is:",m1)
print("Tamil m2 value is:",m2)
print("Maths m3 value is:",m3)
print("science m4 value is:",m4)
print("social m5 value is:",m5)
sum=m1+m2+m3+m4+m5
average=sum/5
print("average=",average)
print("sum of m1,m2,m3,m4 and m5 is:",sum)
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35:
    result ="pass"
    if average >=90:
      grade="o"
    elif average>=80:
      grade="A"
    elif average>=70:
      grade="B"
    elif average>=60:
      grade="C"
    elif average>=50:
      grade="D"
    else:
      grade="E"
else:
    result="fail"
    grade="no grade"
print("result:",result)
print("grade:",grade)
         
