denominator = 64
leftover_inch = 0
mm_constant = 25.4 

def simplify_fraction(num, den):
    while num > 0 and num % 2 == 0 and den % 2 == 0:
        num = num // 2
        den = den // 2
    if num == 0:
        return ""
    return str(num) + "/" + str(den)

# 1. Setup Units
mili_or_inch = input("What is your unit of measurement (millimeters or inches)? ").lower().strip()

# 2. Handle Logic based on user input
user_input = float(input("What is your number to convert? "))

# If user gives inches, we convert to 64ths. 
# If they give mm, we convert mm to inches first (dividing by 25.4), then to 64ths.
if "milli" in mili_or_inch:
    # Converting MM input to inch-64ths
    raw_64ths = (user_input / mm_constant) * 64
else:
    # Converting Inch input to 64ths
    raw_64ths = user_input * 64

# 3. Handle Rounding and Leftovers
rounded_64ths = int(round(raw_64ths))
leftover = raw_64ths - rounded_64ths

# 4. Simplify for Display
whole_inches = rounded_64ths // 64
rem_num = rounded_64ths % 64
fraction_string = simplify_fraction(rem_num, 64)

# 5. Final Print
output = ""

# Only add the whole number if it exists
if whole_inches > 0:
    output += str(whole_inches) + " "

# Add the fraction
output += fraction_string + " inches"

print("Result: " + output)

if leftover != 0:
    # We round this to 4 decimal places so it's not a giant string of numbers

    print("Adjustment made: " + str(round(leftover, 4)) + " (64ths) were rounded.")
