"""Im going to use for else. In most languages,it was like using for and else seperately, but in python there is this concept of using 
for and else together.
let us try with simple example:

"""

nums = [15, 18, 21, 22, 25, 35]
for num in nums:
    print(f"checking if {num} is prime or not?")
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime.")
        break

else:
    print("No prime numbers found in the list")

