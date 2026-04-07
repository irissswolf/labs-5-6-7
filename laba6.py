# 6.1 Функция для проверки делимости на 3
print("1 задание")
def proverka_deleniya_na_3(chislo):
        if chislo % 3 == 0:
            return True
        else:
            return False
print("Проверка делимости числа на 3")
vvedennoe_chislo = int(input("Введите число: "))
rezultat = proverka_deleniya_na_3(vvedennoe_chislo)
if rezultat == True:
        print(f"Число {vvedennoe_chislo} делится на 3")
else:
        print(f"Число {vvedennoe_chislo} не делится на 3")


# 6.2
print("2 задание")
def делить_число(число):
    try:
        result = 100 /число
        return f"Результат: 100 / {число} = {result}"
    except ZeroDivisionError:
        return "Ошибка: На ноль делить нельзя! Введите число, отличное от нуля."
    except TypeError:
        return "Ошибка: Произошла непредвиденная ошибка с типом данных."
try:
    число_пользователя = float(input("Введите число, на которое нужно разделить 100: "))
    result_message = делить_число(число_пользователя)
    print(result_message)
except ValueError:
    print("ошибка: вы ввели не число! введите числовое значение")
except Exception as e:
    print(f"произошла непредвиденная ошибка: {e}")


# 6.3
print("3 задание")
def magic_date(date_string):
    #.split(".") разделяет дату на день,месяц и год
    day_str, month_str, year_str = date_string.split(".")
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)

    последние_две_цифры = year % 100
    #проверка условия: день * месяц=последние две цифры года
    if day * month == последние_две_цифры:
        return True
    else:
        return False
print("проверка магической даты")
print("магическая дата, если день * месяц = две последние цифры года")

дата_пользователя = input("Введите дату в формате ДД.ММ.ГГГГ: ")
result = magic_date(дата_пользователя)
if result:
    print("это магическая дата!")
else:
    print("это не магическая дата")

day, month, year = дата_пользователя.split(".") #вычисления
last_two = int(year) % 100
print(f"\nПроверка: {int(day)} × {int(month)} = {int(day) * int(month)}")
print(f"Последние две цифры года: {last_two}")
print(f"Равенство: {int(day) * int(month)} = {last_two}  {int(day) * int(month) == last_two}")


# 6.4
print("4 задание")
def is_lucky_ticket(ticket_number):
    длина_номера = len(ticket_number)  #len()—находит длину строки
    половина = длина_номера // 2
    первая_половина = ticket_number[:половина] #[:половина]-от начала до индекса половина,не включая его
    вторая_половина = ticket_number[половина:]
    sum_first = 0
    for digit in первая_половина: #цикл для подсчета суммы цифр в первой половине
        sum_first += int(digit)
    sum_second = 0
    for digit in вторая_половина:
        sum_second += int(digit)

    return sum_first == sum_second

ticket = input("Введите номер билета: ")
if len(ticket) % 2 != 0:
    print("Ошибка: номер билета должен содержать чётное количество цифр!")
else:
    result = is_lucky_ticket(ticket)
    print(f"Билет {ticket}: {'СЧАСТЛИВЫЙ' if result else 'НЕ СЧАСТЛИВЫЙ'}")
#проверка для наглядности
    половина = len(ticket) // 2
    первая_сумма = sum(int(d) for d in ticket[:половина])
    вторая_сумма = sum(int(d) for d in ticket[половина:])
    print(f"Сумма первой половины ({ticket[:половина]}): {первая_сумма}")
    print(f"Сумма второй половины ({ticket[половина:]}): {вторая_сумма}")