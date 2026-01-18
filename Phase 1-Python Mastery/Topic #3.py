# Define a function named 'convert_usd_to_eur'
# It accepts one argument: 'amount_usd'
def convert_usd_to_eur(amount_usd):
    # LOCAL VARIABLE: 'conversion_rate' exists only inside this function
    conversion_rate = 0.85
    
    # Calculate the result
    result = amount_usd * conversion_rate
    
    # RETURN the value (send it back to whoever called the function)
    return result

# --- Main Program Logic ---

wallet_usd = 100

# Call the function. 
# We feed it 'wallet_usd' (100). 
# It runs the math and RETURNS 85.0. 
# We catch that returned value in a new variable 'wallet_eur'.
wallet_eur = convert_usd_to_eur(wallet_usd)

print(f"You have ${wallet_usd} USD.")
print(f"That is equal to €{wallet_eur} EUR.")