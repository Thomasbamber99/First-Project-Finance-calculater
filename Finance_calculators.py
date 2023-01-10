import math 
# First choice that the user faces, I  use the .upper function for the first input, this is to ensure the computer recognises what the user enters
print ("investment - Calculates the amount of interest you will earn on your investment portfolio.\n")
print ("bond - Calculates the amount you will have to pay every month for a home loan\n")
choice = input("Choose either 'Investment' or 'Bond' from the menu below to proceed: ").upper()
choice1 = "INVESTMENT"
choice2 = "BOND"

# Conditional checks for inputs from the user
if choice == "INVESTMENT":
    deposit = float(input("Please enter the amount that you are depositing: "))
    
    # Checking whether the user is sure about the amount stored in the input
    check1 =  input((f"You wish to deposit £{deposit}, is this correct? [Yes/No] ")).capitalize()
    if check1 == "No":
        deposit = float(input("Please enter the amount that you are depositing: "))
        
        # Below is if user selects that they are happy with their choice.
    elif    check1 == "Yes":
            user_perc = float(input("Please enter the interest rate. eg 8: "))
            percentage = user_perc / 100
            plan = int(input("How many years do you plan on investing? "))
            interest = input("Would you like to know your simple or compound interest? ").capitalize()
            
            # Formula to work Simple interest
            simple_int = (round(deposit*(1 + percentage * plan),2))
            profit1 = (round(simple_int - deposit,2))
            
            # Formula to work out Compound interest
            comp_int = (round(deposit*((1+ percentage)** plan),2))
            profit2 = (round(comp_int - deposit,2))
            
            if interest == "Simple":
                print (f"Your money will increase to the figure of: £{simple_int} due to simple interest rates. (The total profit is £{profit1})")
            elif interest == "Compound":
                print (f"Your money will have increased to the figure of: £{comp_int} thanks to compound interest. (The total profit is £{profit2})")
                # This next line of code is just incase the user does not enter the right information so the program will run it once again.
            else:
                print ("I'm sorry, I didn't recognise that please try again.\n")
                interest = input("Would you like to know your simple or compound interest? ").capitalize()
                if interest == "Simple":
                    print (f"Your money will increase to the figure of: £{simple_int} due to simple interest rates. (The total profit is £{profit1})")
                elif interest == "Compound":
                    print (f"Your money will have increased to the figure of: £{comp_int} thanks to compound interest. (The total profit is £{profit2}) ")
                
elif choice == "BOND":
    # User inputs
    house_value = float(input("What is the value of your house?: "))
    house_interest = int(input("Please enter the interest rate of the house eg.8: "))
    months = int(input("How many months do you plan on taking to repay the bond? "))
   
    # Forumla for working out repayments using user inputs
    monthly_interest = (house_interest / 100) / 12
    bond_formula = ((house_value * monthly_interest)/(1 -(1 + monthly_interest)**(- months)))
    answer = (round(bond_formula, 2))
    
    print (f"The amount you will pay monthly is: £{answer}")
else:
    print ("I didn't understand that, could you please try again? :)")

# Error message for user to let them know they haven't input the right information :)
  


        
    
    

