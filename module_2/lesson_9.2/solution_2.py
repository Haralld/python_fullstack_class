input_rgb = input("RGB: ")
rgb = [int(x) for x in input_rgb.split(', ')]

def convert_to_hex(rgb):
    
    if len(rgb) != 3:
        print("Ошибка!")
        return None
    
    hex_color = f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
        
    return hex_color

hex_format = convert_to_hex(rgb)
    
print(f"HEX: {hex_format}")


"""
Задача 2: Преобразование RGB в HEX

Описание:

В дизайн-студии Романа часто работают с цветами.
 Цвета в компьютерной графике часто представляются в RGB формате, 
 который состоит из трех чисел: красного (R), зеленого (G) и синего (B).
   Каждый из этих чисел может принимать значения от 0 до 255. Напишите функцию `convert_to_hex`, 
   которая принимает на вход кортеж из трёх чисел (R, G, B) и возвращает цвет в HEX формате.
"""