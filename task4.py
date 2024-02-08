import random
import string

def generate_password(length, num_upper, num_lower, num_digits, num_special):
    total_chars = num_upper + num_lower + num_digits + num_special

    if total_chars > length:
        print("Error: Total number of characters exceeds the specified length.")
        return None

    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digits_chars = string.digits
    special_chars = string.punctuation

    password = []

    password.extend(random.choice(uppercase_chars) for _ in range(num_upper))

   
    password.extend(random.choice(lowercase_chars) for _ in range(num_lower))

  
    password.extend(random.choice(digits_chars) for _ in range(num_digits))

   
    password.extend(random.choice(special_chars) for _ in range(num_special))

   
    remaining_length = length - total_chars
    password.extend(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    # Shuffle the password to randomize the order of characters
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Password Generator")

    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'
    print("\n")
    print("if u are not include any value keep them as the 0 in the below")
    num_upper = int(input("Enter the number of uppercase letters: "))
    num_lower = int(input("Enter the number of lowercase letters: "))
    num_digits = int(input("Enter the number of digits: "))
    num_special = int(input("Enter the number of special characters: "))

    password = generate_password(length, num_upper, num_lower, num_digits, num_special)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()


