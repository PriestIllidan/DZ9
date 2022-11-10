# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;


# Решение в группе: доработанное решение с урока (со скобками)

def calc(exp):
    if exp.find('(') >= 0 and exp.find(')') >= 0:
        # print(exp[:exp.find('(')])
        # print(exp[exp.find(')') + 1:])
        exp = exp[:exp.find('(')] + str(calc(exp[exp.find('(')+1:exp.find(')')])) + exp[exp.find(')') + 1:]
    if exp.find('+') >= 0:
        return calc(exp[:exp.find('+')]) + calc(exp[exp.find('+')+1:])
    if exp.find('-') >= 0:
        return calc(exp[:exp.find('-')]) - calc(exp[exp.find('-')+1:])
    if exp.find('*') >= 0:
        return calc(exp[:exp.find('*')]) * calc(exp[exp.find('*')+1:])
    if exp.find('/') >= 0:
        return calc(exp[:exp.find('/')]) / calc(exp[exp.find('/')+1:])

    return int(exp)


exp = input("Введите арифмитическое выражение: ")
print(calc(exp))
