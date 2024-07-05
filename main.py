# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
number1 = 1234
number2 = 5678
middle_number1 = (number1 // 10) % 100
middle_number2 = (number2 // 10) % 100
sum_middle_numbers = middle_number1 + middle_number2
print(sum_middle_numbers)

# 4th program
number1 = 13.42
number2 = 42.13
int1 = int(number1)
int2 = int(number2)
int1_frac = int((number1 * 100) % 100)
int2_frac = int((number2 * 100) % 100)
print(int1 == int2 or int1 == int1_frac or int1 == int2_frac or int2 == int1_frac or int2 == int2_frac)
