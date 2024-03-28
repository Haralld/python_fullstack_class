# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("""<h1>Добро пожаловать в калькулятор.</h1>
                        <br> Инструкция по работе с калькулятором (все действия выполняются в адресной строке):
                        
                        <br> Для сложения двух чисел необходимо в ввести "первое число" / add / "второе число"
                        <br> Для вычитания двух чисел необходимо в ввести "первое число" / sub / "второе число"
                        <br> Для умножения двух чисел необходимо в ввести "первое число" / mul / "второе число"
                        <br> Для деления двух чисел необходимо в ввести "первое число" / div / "второе число"
""")


def calculator(request, num1, operation, num2):
    result = None
    try:
        if operation == 'add':
            operation = "+"
            result = int(num1) + int(num2)
        elif operation == 'sub':
            operation = "-"
            result = int(num1) - int(num2)
        elif operation == 'mul':
            operation = "*"
            result = int(num1) * int(num2)
        elif operation == 'div':
            if int(num2) == 0:
                return HttpResponse("На ноль делить нельзя, попробуй снова.")
            operation = "/"
            result = int(num1) / int(num2)
        else:
            return HttpResponse("Неверная операция")
        
        return HttpResponse(f"Результат: {num1} {operation} {num2} = {result}")
    except ValueError:
        return HttpResponse("Некорректные данные")