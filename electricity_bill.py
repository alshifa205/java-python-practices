def calculateElectricityCharges(units):
return units * 5

def calculateExtraCharges(units):
return units * 2

(Electricity bill calculator)

def totalBill(units):
electricity = calculateElectricityCharges(units)
extra = calculateExtraCharges(units)
return electricity + extra

def calculateFinalBill(units):
total = totalBill(units)
discount = total * 0.10
return total - discount

def main():
units = 100

total = totalBill(units)
final_bill = calculateFinalBill(units)

print("Electricity Bill Calculator")
print("---------------------------")
print("Units Consumed:", units)
print("Total Bill:", total)
print("Discount:", total * 0.10)
print("Final Payable Amount:", final_bill)

main()