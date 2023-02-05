import math 


def profit(x, y):
    return(round(x - y, 2))

def simple(x, y, z):
    y = y / 100
    return(round(x *(1 + y * z),2))

def compound(x, y, z):
    y = y / 100
    return(round(x *(1 + y ** z),2))

def bond_payments(x, y, z):
    y = (y / 100) / 12
    return((x * y) / (1 - (1 + y) ** (- z)))


print ("investment - Calculates the amount of interest you will earn on your investment portfolio.\n")
print ("bond - Calculates the amount you will have to pay every month for a home loan\n")

answer = input("Choose either 'Investment' or 'Bond' from the menu below to proceed: ").upper()

if answer == "INVESTMENT":
    deposit = float(input("Please enter the amount that you are depositing: "))
    interest = float(input("Please enter the interest rate. eg 8: "))
    plan = int(input("How many years do you plan on investing? "))
    
    interest = input("Would you like to know your simple or compound interest? ").capitalize()
    

    if interest == "Simple":
        result = simple(deposit, interest, plan)
        profit(result, deposit )

        print(f"Your money will increase to the figure of: £{result} due to simple interest rates. (The total profit is £{profit})")
    

    elif interest == "Compound":
        result = compound(deposit, interest, plan)
        profit(result, deposit )

        print (f"Your money will have increased to the figure of: £{result} thanks to compound interest. (The total profit is £{profit})")
    

    else:
        print ("I'm sorry, I didn't recognise that please try again.\n")


elif answer == "BOND":

    house_value = float(input("What is the value of your house?: "))
    house_interest = int(input("Please enter the interest rate of the house eg.8: "))
    months = int(input("How many months do you plan on taking to repay the bond? "))

    result = round(bond_payments(house_value, house_interest, months),2)

    print(f"Your monthly repayments will amount to: £{result}")


else:
    print ("I didn't understand that, could you please try again? :)")
  


        
    
    

