#check if input is valid credit card

def is_valid_credit_card(card_number):
    # Remove spaces and check if all digits
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    # Reverse the digits
    digits = [int(d) for d in card_number][::-1]
    total = 0

    for i, digit in enumerate(digits):
        if i % 2 == 1:  # double every second digit
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

card = input("Enter credit card number: ")

if is_valid_credit_card(card):
    print("✅ Valid Credit Card Number")
else:
    print("❌ Invalid Credit Card Number")
