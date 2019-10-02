TICKET_PRICE = 10

tickets_remaining = 100  

#Run tickets untill its sold out
while tickets_remaining >= 1:

  # Output how many tickets are remaining using the tickets remaining variable
  print("There are {} tickets remaining.".format(tickets_remaining))
  
  # Gather the user's name and assign it to a new variable
  name = input("What is your name? ")
  
  # Prompt the user by name and ask how many tickets they would loke
  num_tickets = input("How many tickets would you like, {}? ".format(name))
  # Catch error when a non number is inputed
  try:
        num_tickets = int(num_tickets) #Coarce it because input() always returns a string
        print(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} remaining".format(tickets_remaining))
  except ValueError as err: # The as err keywords are used only when you have a raise keyword before the except
        print("Sorry an error occured")  
  else:
    # Calculate the price (number of tickets multiplied by the price) and assign it to a variable
        amount_due = num_tickets * TICKET_PRICE
    
    # Output the price in the screen
        print("The total due is ${}".format(amount_due))
    
        should_proceed = input("Do you want to proceed? Y/N ")
        if should_proceed.lower == 'y':
            print('SOLD')
            tickets_remaining -= num_tickets
        else:
            print("Thank you {}".format(name))
    
print("Sorry tickets are sold out")
          
          