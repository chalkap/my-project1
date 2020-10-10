print("Check if Number is odd or even")
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

print("Check if number is large or small")

if num>=1 and num<=10:
    print("too low");

elif num>=11 and num<=20:
    print("medium");   

elif num>=21 and num<=30:
    print("large");

else:
    print("too large")



