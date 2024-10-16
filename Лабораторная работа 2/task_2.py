salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
months = 0
while months != 10:
    months += 1
    money = spend - salary
    money_capital += money
    spend *= 1.03

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")
