# --- Setup and Inputs ---
# Loop until we get a valid denominator
while True:
    try:
        denominator_input = input("What is the denominator you want to use? (e.g., 64): ")
        # Input validation for decimal comma (swapping , for .)
        denominator_input = denominator_input.replace(",", ".")
        
        denominator = int(float(denominator_input)) # Handles if they accidentally type 64.0
        
        if denominator <= 0:
            print("Error: The denominator must be a positive number.")
            continue
            
        break # Success! Break the loop and move to the next part of the code
    except ValueError:
        print("Invalid input! Please enter a number only (no letters).")

mm_constant = 25.4 

def simplify_fraction(num, den):
    """
    Simplifies the fraction by dividing both the numerator and 
    denominator by 2 as long as both numbers remain even.
    """
    while num > 0 and num % 2 == 0 and den % 2 == 0:
        num = num // 2
        den = den // 2
    # If the numerator is 0, we can return an empty string to avoid showing "0/denominator"
    if num == 0:
        return ""
    return str(num) + "/" + str(den)

# 1. Get the unit and value from the user
milli_or_inch = input("What is your unit of measurement (millimeters or inches)? ").lower().strip()
# Input validation 
while True:
    try:
        user_input_raw = input("What is your number to convert? ")
        
        # Handle the decimal comma requirement
        user_input_raw = user_input_raw.replace(",", ".")
        
        user_input = float(user_input_raw)

        if user_input < 0:
            print("Error: Measurements cannot be negative.")
            continue
        
        # Success! Exit the loop
        break 
    except ValueError:
        print("Stupid input detected! Please enter numbers only (decimals allowed).")

# 2. Conversion Logic
# We convert the input into 'raw units' based on the chosen denominator.
if "milli" in milli_or_inch:
    # If millimeters, divide by 25.4 to get inches, then scale by denominator
    raw_units = (user_input / mm_constant) * denominator
else:
    # If inches, just scale by denominator
    raw_units = user_input * denominator

# 3. Rounding and Error Tracking
rounded_units = int(round(raw_units))
leftover = raw_units - rounded_units

# 4. Breaking down the total units into Whole Inches and the Fractional Remainder
whole_inches = rounded_units // denominator
rem_num = rounded_units % denominator

# 5. Simplifying the fraction (e.g., turning 16/64 into 1/4)
fraction_string = simplify_fraction(rem_num, denominator)

# 6. Building the Final Output String
output = ""

# Only add the whole number if it's greater than 0
if whole_inches > 0:
    output += str(whole_inches)
    # Add a space only if there is a fraction following the whole number
    if fraction_string != "":
        output += " "

# Add the fraction and the unit label
if fraction_string != "":
    output += fraction_string
elif whole_inches == 0:
    # This handles the case where the user inputs 0
    output += "0"

output += " inches"

# --- Display Results ---
print("\n" + "-"*30)
print("Result: " + output)

# Only show the adjustment if there actually was a rounding difference
if leftover != 0:
    # The leftover is expressed in terms of your chosen denominator
    print("Adjustment made: " + str(round(leftover, 4)) + " (" + str(denominator) + "ths) were rounded.")
print("-"*30)
