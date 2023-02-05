def profit(x, y):
    return(round(x - y, 2))

def simple(x, y, z):
    return(round(x *(1 + y * z),2))

def compound(x, y, z):
    return(round(x *(1 + y ** z),2))

def bond_payments(x, y, z):
    return((x * y) / (1 - (1 + y) ** (- z)))


print ("investment - Calculates the amount of interest you will earn on your investment portfolio.\n")
print ("bond - Calculates the amount you will have to pay every month for a home loan\n")

answer = input("Enter either: --> 'I' for'Investment'\n\t\t--> 'B' for 'Bond' from the menu below to proceed: ").upper()

if answer == "I":
    deposit = int(input("\nPlease enter the amount that you are depositing: "))
    time = int(input("How many years do you plan on investing? "))
    rate = int(input("Please enter the interest rate. eg 8: "))

    int_rate = rate / 100
    
    
    interest = input("\nWould you like to know your simple or compound interest? \n").capitalize()
    

    if interest == "Simple":
        result = simple(deposit, int_rate, time)
        profit1 = profit(result, deposit )

        print(f"Your money will increase to the figure of: £{result} due to simple interest rates. (The total profit is £{profit1})")
    

    elif interest == "Compound":
        result = compound(deposit, int_rate, time)
        profit2 = profit(result, deposit )

        print (f"Your money will have increased to the figure of: £{result} thanks to compound interest. (The total profit is £{profit2})")
    

    else:
        print ("I'm sorry, I didn't recognise that please try again.\n")


elif answer == "B":

    house_value = float(input("\nWhat is the value of your house?: "))
    interest= int(input("Please enter the interest rate of the house eg.8: "))
    length = int(input("How many months do you plan on taking to repay the bond? "))
    
    monthly_interest = (interest / 100) / 12

    result = round(bond_payments(house_value, monthly_interest, length),2)

    print(f"\nYour monthly repayments will amount to: £{result}")


else:
    print ("I didn't understand that, could you please try again? :)")
  


        
    
    

