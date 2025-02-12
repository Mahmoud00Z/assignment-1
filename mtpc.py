print("\tWelcome to the Movie Ticket Price calculator")
age = int(input("please enter your age : "))
price = 5
if age > 64 :
    print(f"Your ticket price is {price}$")
elif age > 24 :
    print(f"Your ticket price is {price + 2}$")
elif age > 18 :
    print(f"Your ticket price is {price + 1}$")
elif age > 13 :
    print(f"Your tivket price is {price}$")
else :
    print(f"Your ticket price is {price - 1}$")
            