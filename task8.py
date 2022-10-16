money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

deficit = salary - spend
while money_capital + deficit >= spend:
    money_capital += deficit
    spend = spend * (increase + 1)
    month += 1

print(month)

