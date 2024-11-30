# Banknotes

number = int(input())


original_number = number


hundreds = fifth = quarters = tens = fives = two = ones = 0


while number >= 100:
    number -= 100
    hundreds += 1

while number >= 50:
    number -= 50
    fifth += 1

while number >= 20:
    number -= 20
    quarters += 1

while number >= 10:
    number -= 10
    tens += 1

while number >= 5:
    number -= 5
    fives += 1

while number >= 2:
    number -= 2
    two += 1

while number >= 1:
    number -= 1
    ones += 1


print(f"{original_number}")


print(f"{hundreds} nota(s) de R$ 100,00")
print(f"{fifth} nota(s) de R$ 50,00")
print(f"{quarters} nota(s) de R$ 20,00")
print(f"{tens} nota(s) de R$ 10,00")
print(f"{fives} nota(s) de R$ 5,00")
print(f"{two} nota(s) de R$ 2,00")
print(f"{ones} nota(s) de R$ 1,00")
