# --- Setup ---
mm_constant = 25.4 

def simplify_fraction(num, den):
    while num > 0 and num % 2 == 0 and den % 2 == 0:
        num = num // 2
        den = den // 2
    if num == 0: return ""
    return str(num) + "/" + str(den)

# --- USER INTERFACE: Header ---
print("=======================================")
print("   PRECISION MEASUREMENT CONVERTER")
print("=======================================")
print("This tool converts MM or Inches into")
print("the cleanest possible fraction.")
print("---------------------------------------\n")

# --- UI: Input Section ---
# (Using the validation loops we built earlier)
while True:
    try:
        den_raw = input("STEP 1: Enter desired precision (e.g. 16, 32, 64): ")
        denominator = int(float(den_raw.replace(",", ".")))
        if denominator <= 0:
            print("(!) Please enter a positive number.")
            continue
        break
    except ValueError:
        print("(!) Invalid input. Numbers only, please.")

while True:
    unit_input = input("STEP 2: Is your input in Millimeters or Inches? ").lower().strip()
    if "milli" in unit_input or "inch" in unit_input:
        break
    print("(!) Please type 'milli' or 'inch'.")

while True:
    try:
        val_raw = input("STEP 3: Enter the value to convert: ")
        user_input = float(val_raw.replace(",", "."))
        break
    except ValueError:
        print("(!) Stupid input detected. Please use numbers.")

# --- Math Logic ---
if "milli" in unit_input:
    raw_units = (user_input / mm_constant) * denominator
else:
    raw_units = user_input * denominator

rounded_units = int(round(raw_units))
leftover = raw_units - rounded_units
whole_inches = rounded_units // denominator
rem_num = rounded_units % denominator
fraction_string = simplify_fraction(rem_num, denominator)

# --- USER INTERFACE: Result Section ---
print("\n" + "="*39)
print("             FINAL RESULT")
print("="*39)

output = ""
if whole_inches > 0:
    output += str(whole_inches)
    if fraction_string != "": output += " "

if fraction_string != "":
    output += fraction_string
elif whole_inches == 0:
    output += "0"

print("         >>> " + output + " inches <<<")
print("="*39)

if leftover != 0:
    print("\n[Technical Note]")
    print("Adjustment: " + str(round(leftover, 4)) + " (" + str(denominator) + "ths) rounded.")
