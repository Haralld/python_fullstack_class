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
# http://127.0.0.1:5000/sum 
@app.route('/sum/<float:x>/<float:y>') # сложение
def sum(x, y):
    return f'{x} + {y} = {x + y}'
        
# http://127.0.0.1:5000/sub
@app.route('/sub/<float:x>/<float:y>')    # вычитание
def sub(x, y):
    return f'{x} - {y} = {x - y}'

# http://127.0.0.1:5000/mul
@app.route('/mul/<float:x>/<float:y>')    # умножение
def mul(x, y):
    return f'{x} * {y} = {x * y}'

# http://127.0.0.1:5000/div
@app.route('/div/<float:x>/<float:y>')    # деление
def div(x, y):
    if y != 0:
        return f'{x} / {y} = {x / y}'        
    else:
        return 'На ноль делить нельзя'

if __name__ == '__main__':
    app.run()
    
