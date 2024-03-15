import string, random

print("Welcome to the Password Generator!")
total = int(input("Enter the total of number of character in the password: "))
letter = int(input("Enter the number of letters in the password: "))
number = int(input("Enter the number of numbers in the password: "))
symbol = int(input("Enter the number of symbols in the password: "))

if letter+number+symbol == total:
    Generated_letter = (
        random.choices(string.ascii_letters, k=letter)+
        random.choices(string.digits, k=number)+
        random.choices(string.punctuation, k=symbol)
    )
    random.shuffle(Generated_letter)
    Generated_Password = ''.join(Generated_letter)
    print(f"Generated Password: {Generated_Password}")
else:
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password.")
