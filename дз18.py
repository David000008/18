tickets = int(input('Введите количество билетов: '))
back = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст участника №{i + 1}: '))
    back.append(input_value)
    def prise(back):
        if back < 18:
            return 0
        elif 18 <= back < 25:
            return 990
        else:
            return 1390
    full_prise = sum(map(prise, back))
discount_prise = int(full_prise * 0.9)
if tickets > 3:
    print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
else:
    print('Стоимость всех билетов: ', full_prise, "руб.")