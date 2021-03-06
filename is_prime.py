# This is a simple program that determines if a
# number is prime or not.
def is_prime(x):
    n=int(x)         #converts the input number to int
    a=2
    if n<=1:         #All numbers less than or equal to 1 are not prime
        return False
    elif n==2:       # 2 not prime
        return True
    else:
        while a in range(2,n-1):
            if n%a==0:
                return False
                break
            else:
                a=a+1
        return True
while True:
    try:
        input_num=int(input("Enter your number:"))
    except ValueError:
        #The following message will be displayed
        # if the use input non integers
        print("You didn't enter an integer")
        continue
    else:
        break
if is_prime(input_num)==True:
    print("Your number is prime")
else:
    print("Your number is not prime")