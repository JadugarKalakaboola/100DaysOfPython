print("\n\n********** Welcome To Bill Calculator **********\n\n")

bill = float(input("Enter bill amount: $"))
tip_percentage = int(input("Enter tip percentage (10, 12, 15): "))
total_people = int(input("Enter total number of people: "))

tip_amount = bill * tip_percentage / 100

total_amount = bill + tip_amount

bill_per_person = round(total_amount / total_people, 2)

print(f"\n\n********** BILL **********\n\nTotal Bill: {bill} \nBill + Tip: {bill} + {tip_amount} = {total_amount}\nBill per person: ${bill_per_person}\n\n********** END **********\n\n")

