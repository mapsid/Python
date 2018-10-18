print("Enter a number")
answer=input()

n=int(answer)
a=n
sum=0
d=0

while n>0:
    d=n%10
    sum=sum+d**3
    n=n/10

if sum==a:
    print(a, "is an Armstrong number")
else:
    print(a, "is not an armstrong number")
