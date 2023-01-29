import complex_number
import rational_number
import view
import log


def operation(a=0, b=0, t=0):
    t = view.type_input()
    if t == 0:
        print('Введено неверно, попробуйте ещё раз.\n')
        return operation()
    tp = 'рациональными' if t == 1 else 'комплексными'
    print(f'Работаем с {tp} числами.')
    a = view.number_input(0)
    b = view.number_input(1)
    return a, b, t


def result(a, b, t):
    o = view.operator_input()
    itog = rational_number.irrattional_operation(a, b, o) if t == 1 \
        else complex_number.complex_operation(a, b, o)
    if not itog:
        print('Введено неверно, попробуйте ещё раз. (+,-,*,/)\n ')
        return result(a, b, t)
    print(f'{a} {o} {b} = {itog}')
    return (f'{a} {o} {b} = {itog}')


def calculate():
    a, b, t = operation()
    log.write_log(result(a, b, t))