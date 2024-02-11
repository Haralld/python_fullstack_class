from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"

# для обработки принемаймой полезной нагрузки ввиде параметра типа данных string
# http://127.0.0.1:5000/name/Ivan
@app.route('/name/<s>')
def show_string(s):
    print(type(s))
    return f'Hello, {s}'

# для обработки числовых параметров
# http://127.0.0.1:5000/add 
@app.route('/<x>/<y>/add') # сложение
def add(x, y):
    x, y = float(x), float(y)
    return f'{x} + {y} = {x + y}'
        
# http://127.0.0.1:5000/sub
@app.route('/<x>/<y>/sub')    # вычитание
def sub(x, y):
    x, y = float(x), float(y)
    return f'{x} - {y} = {x - y}'

# http://127.0.0.1:5000/mul
@app.route('/<x>/<y>/mul')    # умножение
def mul(x, y):
    x, y = float(x), float(y)
    return f'{x} * {y} = {x * y}'

# http://127.0.0.1:5000/div
@app.route('/<x>/<y>/div')    # деление
def div(x, y):
    x, y = float(x), float(y)
    if y:
        return f'{x} / {y} = {x / y}'        
    else:
        return 'На ноль делить нельзя'

if __name__ == '__main__':
    app.run()
    
