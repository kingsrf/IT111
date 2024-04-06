
TAX_RATE = 0.1

# Input
name = input("What is your name? ")
amount = float(input("What is the amount of your purchase? "))

# Calculations
tax = amount * TAX_RATE
total = tax + amount

# Output
print("\nHello", name + ", here is your sales receipt:")
print("Subtotal = $", format(amount, '7.2f'))
print("     Tax = $", format(tax, '7.2f'))
print(" " * 12 + "-" * 8)
print("   Total = $", format(total, '7.2f'))
