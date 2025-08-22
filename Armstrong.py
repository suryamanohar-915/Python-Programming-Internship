n=int(input("Enter a number: "))
b=n
length=len(str(b))
sum=0
while n!=0:
    rem=n%10
    sum=sum+(rem**length)
    n=n//10
if(sum==b):
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
