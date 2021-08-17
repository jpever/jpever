# this is the calc to display the bill amount when dine in , which share bill with friends.
print("Welcome to the tip calculator.")

bill = input("What was the total bill? " + '$')
people = input("how many people to split the bill? ")

# tip percentage

tip = input("What percentage tip would you lile to give? 0, 10, 12 or 15? ")
tip_bill = float(tip) / 100  # calc tip % / 100
total = float(bill) * tip_bill  # bill + tip
total_bill = float(bill) + total
final = int(total_bill) / int(people)  # total dived by each member
print("Each person should pay:$ ", final)
