# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
# result = round((bill + bill * (tip / 100)) / people , 2)
# print(f"Each person should pay : ${result}")


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
amount = (tip / 100 + 1 ) * bill / people
# tip이 백분률이므로 100으로 나누고 1을 더한 값을 곱하면 bill 금액에 tip을 더한 금액 산출 됨
print(amount)
print(round(amount, 2))
print(f"Each person should pay: ${round(amount, 2)}")
