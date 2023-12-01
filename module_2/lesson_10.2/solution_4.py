input_budget = float(input("Бюджет: "))

def choose_ad_platform(input_budget):
    if input_budget < 1000:
        selection = "Google"
    elif 1000 <= input_budget < 5000:
        selection = "Facebook"
    elif 5000 <= input_budget:
        selection = "Instagram"
    return selection    
                     
result = choose_ad_platform(input_budget)

print(result)

"""
Задача 4: Выбор рекламной платформы

Описание: Роман хочет определить, какую рекламную платформу выбрать для следующей рекламной кампании своего магазина.
 Он рассматривает три варианта: Google, Facebook и Instagram. 
 Роман считает, что выбор платформы зависит от следующих параметров:

- Если бюджет меньше 1000$, то выбрать Google

- Если бюджет от 1000$ до 5000$, то выбрать Facebook.

- Если бюджет больше 5000$, то выбрать Instagram.



Напишите функцию `choose_ad_platform`, которая принимает на вход бюджет и возвращает название рекламной платформы.


"""